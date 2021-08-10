def collect_rules():
    rules = []

    # use dynamic import to prevent circular dependencies when module is loaded
    import bids.rules.rules_files as sr
    rules.append(sr.TopLevelFilesValidationRule)
    rules.append(sr.AssociatedDataValidationRule)
    rules.append(sr.EntitiesValidationRule)
    rules.append(sr.DatatypesValidationRule)

    return rules
