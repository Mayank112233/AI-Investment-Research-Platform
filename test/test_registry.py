from tools.registry import ToolRegistry

def main():
    registry = ToolRegistry()

    print("\nRegistered Tools:")
    print("-" * 40)

    for tool in registry.list_tools():
        print(tool)

if __name__ == "__main__":
    main()