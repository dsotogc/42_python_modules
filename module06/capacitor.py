from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability


def main() -> None:
    print("Testing Creature with transform capability")
    t_factory = TransformCreatureFactory()
    base = t_factory.create_base()
    evolved = t_factory.create_evolved()
    for stage, creature in [("base", base), ("evolved", evolved)]:
        print(f"{stage}:")
        print(creature.describe())
        print(creature.attack())
        if not isinstance(creature, TransformCapability):
            raise TypeError("Factory returned a creature without transform")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    main()
