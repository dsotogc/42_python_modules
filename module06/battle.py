from ex3 import FlameFactory, TransformCreatureFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    b1 = f1.create_base()
    b2 = f2.create_base()
    print(f"{b1.describe()}\nvs\n{b2.describe()}")
    print("fight!")
    print(b1.attack())
    print(b2.attack())


def main() -> None:
    f_factory = FlameFactory()
    tc_factory = TransformCreatureFactory()
    test_factory(f_factory)
    print()
    test_factory(tc_factory)
    print()
    test_battle(f_factory, tc_factory)


if __name__ == "__main__":
    main()
