from functools import reduce


def main():
    from pathlib import Path

    input_path = Path(__file__).parent / "answers.txt"

    with input_path.open('r') as fp:
        groups = fp.read().strip().split("\n\n")

    # part 1
    answers = [len(set(group.replace("\n", ""))) for group in groups]
    print(sum(answers))

    # part 2
    def agg(intersect, answers):
        return answers if intersect is None else intersect & answers

    intersect_answers = [
        reduce(agg, map(set, group.split("\n")))
        for group in groups
    ]

    print(reduce(lambda count, ans: count + len(ans), intersect_answers, 0))


if __name__ == "__main__":
    main()
