
from html.parser import HTMLParser

class FormTest(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.has_form = False
        self.has_submit = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.has_form = True

        if tag == "input":
            if attrs.get("id"):
                self.ids.add(attrs["id"])

        if tag == "button" and attrs.get("type") == "submit":
            self.has_submit = True

with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

test = FormTest()
test.feed(html)

assert test.has_form, "FAIL: Form is missing"
assert "name" in test.ids, "FAIL: Name field is missing"
assert "email" in test.ids, "FAIL: Email field is missing"
assert "contact" in test.ids, "FAIL: Contact Number is missing"
assert test.has_submit, "FAIL: Submit button is missing"

print("PASS: Form is present")
print("PASS: Name field is present")
print("PASS: Email field is present")
print("PASS: Contact Number field is present")
print("PASS: Submit button is present")
print("ALL TESTS PASSED")
