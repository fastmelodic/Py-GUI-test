

def test_delete_last_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group('Test_group')
    old_list = app.groups.get_group_list()
    app.groups.delete_group(-1)
    new_list = app.groups.get_group_list()
    assert sorted(old_list[:-1]) == sorted(new_list)