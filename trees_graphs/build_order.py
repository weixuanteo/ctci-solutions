# You are given a list of projects and a list of dependencies (which is a list of pairs),
# where the first element in each pair is a project that must be built before the second project is built.
# Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c


def create_build_order(projects: list[str], dependencies: list[tuple]) -> list[str]:
    graph = create_directed_graph(projects, dependencies)
    indegree = build_indegree(graph)
    build_order = []
    stack = []

    for p in indegree:
        if indegree[p] == 0:
            stack.append(p)

    while stack:
        p = stack.pop()
        build_order.append(p)
        for d in graph[p]:
            indegree[d] -= 1
            if indegree[d] == 0:
                stack.append(d)

    if not is_valid_order(build_order, projects):
        return None

    return build_order


def create_directed_graph(projects: list[str], dependencies: list[tuple]) -> dict:
    graph = {}
    for p in projects:
        graph[p] = []
    for d in dependencies:
        graph[d[0]].append(d[1])
    return graph


def build_indegree(graph: dict) -> dict:
    indegree = {}
    for p in graph:
        indegree[p] = 0
    for p in graph:
        for d in graph[p]:
            indegree[d] += 1
    return indegree


def is_valid_order(build_order: list[str], projects: list[str]) -> bool:
    return len(build_order) == len(projects)


def main():
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    build_order = create_build_order(projects, dependencies)
    print(build_order)


if __name__ == "__main__":
    main()
