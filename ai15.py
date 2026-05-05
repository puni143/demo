rules=[
    (["A","B"],"C"),
    (["C"],"D"),
    (["D"],"E")
    ]

facts=["A","B"]
def forward_chaining(rules,facts):
    inferred=True
    while inferred:
        inferred=False
        for conditions,conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.append(conclusion)
                    print("inferred facts:",facts)
                    inferred=True

    return facts
print("initial facts:",facts)
final_facts=forward_chaining(rules,facts)
print("final facts:",final_facts)
