# db_manager.py
#
#
# class DBManager:
#     def __init__(self):
#         pass
#
#     def get_by_id(self, entry_id):
#         return Entry.query.filter_by(id=entry_id).first_or_404()
#
#
# db_manager = DBManager()
#
#
# @pytest.fixture
# def entry():
#     entry_id = create_entry(title="xxxxx")
#     return Entry.get_by_id(entry_id)
#
#
# def test_create_entry():
#     entry_id = create_entry(title="xxxxx")
#     entry = Entry.get_by_id(entry_id)
#     assert entry.title == "xxxxx"
#     assert entry.is_published == False
#
#
# def test_publishing():
#     entry_id = create_entry(title="xxxxx")
#     entry = Entry.get_by_id(entry_id)
#     entry.set_published()
#     assert entry.is_published == True
#
#
# def test_edit():
#     entry_id = create_entry(title="xxxxx")
#     entry = Entry.get_by_id(entry_id)
#     ...