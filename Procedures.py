# page = contents of a web page
page = ('<div id="top_bin"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')  # finds the string '<a href=' in var page
start_quote = page.find('"', start_link)  # finds the first " located after the end of var start_link
end_quote = page.find('"', start_quote + 1)  # finds the 2nd " located after var start_quote +1 (h)
url = page[start_quote + 1: end_quote]  # creates the var "url" and selects the string between
print(url)  # prints var url


# Automates above to find all links in the page

def get_next_target(page):
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return [url, end_quote]

print(get_next_target(page))


# Basic procedure w/ input -----------------------------

def rest_of_string(s):  # Creates the procedure "rest_of_string" with the input s.
    return s[:]  # Same as string-in-string [1:] = "est", etc...


print(rest_of_string('test'))  # Sets (s) in line 23 to the string "test" and prints depending on "return s[#:#]"


def sum(a, b):  # a becomes s and b becomes t, they still return for a
    a = a + b
    return a

s = 'Hello '
t = 'Mike!'
print(sum(s, t))


def abbaize(a, b):  # var's (input's) are contained within the def
    return a + b + b + a  # composition of var's

print(abbaize('a', 'b'))  # strings
print(abbaize('cat', 'dog'))  # strings


# --------------------------------------------------------
# Procedure Composition

def square(n):
    return n * n

x = 5
print(square(square(x)))


def find_second(search, target):
    return search.find(target, search.find(target) + 1)

space = "somewhere something is looking to be found somewhere"
print(find_second(space, 'somewhere'))

