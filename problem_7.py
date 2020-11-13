import collections


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = collections.defaultdict(RouteTrieNode)

    def insert(self, path):
        return self.children[path]


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, steps, handler):
        current = self.root
        for step in steps:
            current = current.insert(step)

        current.handler = handler

    def find(self, steps):
        current = self.root
        for step in steps:
            if step in current.children:
                current = current.children[step]
            else:
                return None

        return current


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.not_found_handler = not_found_handler

        self.routes = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        self.routes.insert(self.split_path(path), handler)

    def lookup(self, path):
        route = self.routes.find(self.split_path(path))
        if route is None or route.handler is None:
            return self.not_found_handler

        return route.handler

    def split_path(self, path):
        if not isinstance(path, str):
            raise ValueError("Path should be a string")

        steps = path.split('/')
        if steps[0] == '':
            steps = steps[1:]  # get rid of first /
        else:
            raise ValueError('Path should start with /')

        while steps and steps[-1] == '':
            steps = steps[:-1]  # get rid of last /

        return steps

router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

# Edge cases
print(router.lookup("////"))  # should print 'root handler'
print(router.lookup("")) # should print 'root handler'

try:
    router.lookup("home/about")
except ValueError as e:
    print(e) # Path should start with /

try:
    router.lookup(None)
except ValueError as e:
    print(e)  # Path should be a string
