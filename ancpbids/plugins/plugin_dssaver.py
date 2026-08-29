import inspect

import ancpbids
from ancpbids.plugin import WritingPlugin, hook
from ancpbids.vfs import resolve_vfs


@hook(ranking=0, system=True)
class DatasetWritingPlugin(WritingPlugin):
    def execute(self, ds, target_dir: str, context_folder=None, src_dir: str = None, vfs=None):
        resolved_vfs = resolve_vfs(vfs)
        if context_folder is None and resolved_vfs.exists(target_dir) and len(resolved_vfs.listdir(target_dir)) > 0:
            raise ValueError("Directory not empty: " + target_dir)

        # set the target_dir as the base directory for creation
        if not hasattr(ds, 'base_dir_') or ds.base_dir_ is None:
            ds.base_dir_ = target_dir

        if context_folder is None:
            context_folder = ds
        if src_dir is None:
            src_dir = ds.get_absolute_path()

        self.schema = ds.get_schema()

        generator = context_folder.to_generator()
        for obj in generator:
            typ = type(obj)
            mapper_name = '_type_handler_' + typ.__name__
            if mapper_name not in _TYPE_MAPPERS:
                mapper_name = '_type_handler_default'
            mapper = _TYPE_MAPPERS[mapper_name]
            mapper(self, src_dir, target_dir, obj, resolved_vfs)
        # copy internal children (files/folders)
        self._type_handler_Folder(src_dir, target_dir, context_folder, resolved_vfs, traverse_children=True)

    def _type_handler_default(self, src_dir, target_dir, obj, vfs):
        if isinstance(obj, self.schema.Folder):
            self._type_handler_Folder(src_dir, target_dir, obj, vfs)
        elif isinstance(obj, self.schema.File):
            self._type_handler_File(src_dir, target_dir, obj, vfs)

    def _type_handler_File(self, src_dir, target_dir, file, vfs, new_file_name=None):
        abs_file_name = file.get_absolute_path()
        dir_name = vfs.dirname(abs_file_name)
        if not vfs.exists(dir_name):
            vfs.makedirs(dir_name)

        content = getattr(file, 'content', None)
        if callable(content):
            content(abs_file_name)
            return

        if content is not None:
            ancpbids.utils.write_contents(abs_file_name, content, vfs=vfs)
            return

        # Prefer an explicit contents payload over dumping the whole model.
        payload = getattr(file, '_contents', None)
        if payload is None and hasattr(file, 'get'):
            payload = file.get('contents')
        if payload is not None and not callable(payload):
            ancpbids.utils.write_contents(abs_file_name, payload, vfs=vfs)
            return

        ancpbids.utils.write_contents(abs_file_name, file, vfs=vfs)

    def _type_handler_Folder(self, src_dir, target_dir, folder, vfs, traverse_children=False):
        new_dir = vfs.join(target_dir, folder.get_relative_path())
        if not vfs.exists(new_dir):
            vfs.makedirs(new_dir)

        if traverse_children:
            for child_folder in folder.folders:
                self._type_handler_Folder(src_dir, target_dir, child_folder, vfs)
            for child_file in folder.files:
                self._type_handler_File(src_dir, target_dir, child_file, vfs)

    def _get_ordered_entity_keys(self, artifact):
        schema = artifact.get_schema()
        schema_entities = list(map(lambda e: e.value['name'], list(schema.EntityEnum)))
        expected_key_order = {k: i for i, k in enumerate(schema_entities)}
        expected_order_key = {i: k for i, k in enumerate(schema_entities)}

        artifact_keys = list(artifact.entities)
        actual_keys_order = list(map(lambda k: expected_key_order[k], artifact_keys))
        expected = tuple(map(lambda k: expected_order_key[k], sorted(actual_keys_order)))
        return expected

    def _type_handler_Artifact(self, src_dir, target_dir, artifact, vfs):
        segments = []
        schema = artifact.get_schema()
        # add missing entities
        for ancestor in artifact.iterancestors():
            if isinstance(ancestor, schema.Folder):
                name = ancestor.name
                if name.startswith("ses-"):
                    artifact.add_entity('ses', name[4:])
                if name.startswith("sub-"):
                    artifact.add_entity('sub', name[4:])

        # sort according order defined in schema
        ordered_keys = self._get_ordered_entity_keys(artifact)
        for ok in ordered_keys:
            seg = '-'.join([ok, str(artifact.get_entity(ok))])
            segments.append(seg)
        segments.append(artifact.suffix)
        new_file_name = '_'.join(segments) + artifact.extension
        artifact.name = new_file_name
        self._type_handler_File(src_dir, target_dir, artifact, vfs, new_file_name)


_TYPE_MAPPERS = {name: obj for name, obj in inspect.getmembers(DatasetWritingPlugin) if
                 inspect.isfunction(obj) and obj.__name__.startswith('_type_handler_')}


def write_artifact(artifact, vfs=None):
    dummy_inst = DatasetWritingPlugin()
    dummy_inst._type_handler_Artifact(None, None, artifact, resolve_vfs(vfs))
    return artifact.get_absolute_path()
