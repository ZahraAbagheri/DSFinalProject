class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class YFastTrie:
    def __init__(self):
        self.root = TrieNode()
        self.words_count = 0
# تعداد کلمات در  Trie
    def add(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        if not current_node.is_end_of_word:
            current_node.is_end_of_word = True
            self.words_count += 1
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word
    def delete(self, word):
        def _delete_helper(node, word, depth):
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    return True
                return False
            char = word[depth]
            if char in node.children:
                if _delete_helper(node.children[char], word, depth + 1):
                    if not node.children[char].children and not node.children[char].is_end_of_word:
                        del node.children[char]
                        return True
                return False
        if self.search(word) :
            _delete_helper(self.root, word, 0)
            self.words_count -= 1 #کاهش تعداد کلمات پس از حذف


        return False
        if self.search(word):
            _delete_helper(self.root, word, 0)
            self.words_count -= 1
    def get_words_count(self):
        return self.words_count
# مثال استفاده:

trie = YFastTrie()
words = ["apple", "application", "apply", "orange", "banana"]

# اضافه کردن کلمات به   Trie

for word in words:
    trie.add(word)
# جستجو

print(trie.search("apple"))
# True
print(trie.search("app"))
# False
# حذف
trie.delete("apple")
print(trie.search("apple"))
# False
#تعدادکلمات

print(trie.get_words_count())

# 4 (باقی‌مانده:application, apply, orange, banana)