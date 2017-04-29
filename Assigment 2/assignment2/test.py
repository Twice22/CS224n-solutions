    partial_parses = [PartialParse(s) for s in sentences]
    unfinished_parses = partial_parses.copy()

    while unfinished_parses:
        transitions = model.predict(unfinished_parses[:batch_size])
        for i in range(min(batch_size, len(unfinished_parses))):
            unfinished_parses[i].parse_step(transitions[i])
        unfinished_parses = [p for p in unfinished_parses if not(len(p.stack) == 1 and len(p.buffer) == 0)]

    dependencies = [p.dependencies for p in partial_parses]