from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with transform capability")
    t_factory: CreatureFactory = TransformCreatureFactory()
    base = t_factory.create_base()
    evolved = t_factory.create_evolved()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()