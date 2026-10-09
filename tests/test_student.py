import pytest

from student import Student, StudentManager, is_valid_email


@pytest.fixture
def manager():
    m = StudentManager()
    m.add_student(Student(1, "Aarav Sharma", "aarav.sharma@vcet.edu.in", "AI&DS"))
    m.add_student(Student(2, "Priya Patil", "priya.patil@vcet.edu.in", "AI&DS"))
    return m


def test_add_student(manager):
    manager.add_student(Student(3, "Rohan Mehta", "rohan.mehta@vcet.edu.in", "COMP"))
    assert manager.count() == 3
    assert manager.get_student(3).name == "Rohan Mehta"


def test_duplicate_roll_no_rejected(manager):
    with pytest.raises(ValueError):
        manager.add_student(Student(1, "Someone Else", "someone@vcet.edu.in", "IT"))


def test_get_missing_student_returns_none(manager):
    assert manager.get_student(99) is None


def test_remove_student(manager):
    removed = manager.remove_student(2)
    assert removed.name == "Priya Patil"
    assert manager.count() == 1


def test_remove_missing_student_raises(manager):
    with pytest.raises(KeyError):
        manager.remove_student(99)


def test_list_students_sorted_by_roll_no(manager):
    manager.add_student(Student(5, "Neha Joshi", "neha.joshi@vcet.edu.in", "IT"))
    assert [s.roll_no for s in manager.list_students()] == [1, 2, 5]


@pytest.mark.parametrize("roll_no, name, course", [
    (0, "Aman Verma", "IT"),
    (-4, "Aman Verma", "IT"),
    (7, "   ", "IT"),
    (7, "Aman Verma", ""),
])
def test_invalid_student_rejected(manager, roll_no, name, course):
    with pytest.raises(ValueError):
        manager.add_student(Student(roll_no, name, "aman.verma@vcet.edu.in", course))
    assert manager.count() == 2


@pytest.mark.parametrize("email", ["aarav.sharma@vcet.edu.in", "neha_j+lab@gmail.com"])
def test_valid_emails(email):
    assert is_valid_email(email)


@pytest.mark.parametrize("email", ["", "neha.joshi", "neha@", "@vcet.edu.in", "neha joshi@vcet.in"])
def test_invalid_email_rejected(manager, email):
    assert not is_valid_email(email)
    with pytest.raises(ValueError):
        manager.add_student(Student(8, "Neha Joshi", email, "IT"))
