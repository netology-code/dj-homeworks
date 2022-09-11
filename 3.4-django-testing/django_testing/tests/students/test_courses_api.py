import random

from model_bakery import baker
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.test import APIClient
import pytest

from students.models import Student, Course
from django_testing import settings

settings.MAX_STUDENTS_PER_COURSE = 3


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, courses_factory):
    # Arrange
    course = courses_factory(_quantity=1)

    # Act
    response = client.get(f'/api/v1/courses/{course[0].id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_get_courses(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_get_filter_courses(client, courses_factory):
    # Arrange
    course = courses_factory(_quantity=10)
    id = course[random.randint(0, 10)].id
    name = course[random.randint(0, 10)].name

    # Act
    response_id = client.get(f'/api/v1/courses/?id={id}')
    response_name = client.get(f'/api/v1/courses/?name={name}')

    # Assert
    assert response_id.status_code == 200
    assert response_name.status_code == 200
    data_id = response_id.json()
    data_name = response_name.json()
    assert data_id[0]['id'] == id
    assert data_name[0]['name'] == name


@pytest.mark.parametrize(
    ["students_count", "expected_status"],
    ((1, HTTP_201_CREATED),
     (5, HTTP_400_BAD_REQUEST),
     (0, HTTP_201_CREATED),
     )
    )
@pytest.mark.django_db
def test_create_course(client, students_factory, students_count, expected_status):
    count = Course.objects.count()
    if students_count > 0:
        students = students_factory(_quantity=students_count)
        students_id = [student.id for student in students]
    else:
        students_id = []
        count += 1

    response = client.post('/api/v1/courses/', data={'name': 'Any_course', 'students': students_id})

    assert response.status_code == expected_status
    if response.status_code == HTTP_201_CREATED:
        assert Course.objects.count() == count + students_count


@pytest.mark.parametrize(
    ["students_count", "expected_status"],
    ((1, HTTP_200_OK),
     (5, HTTP_400_BAD_REQUEST),
     )
    )
@pytest.mark.django_db
def test_update_course(client, students_factory, courses_factory, students_count, expected_status):
    course = courses_factory(_quantity=1)
    if students_count > 0:
        students = students_factory(_quantity=students_count)
        students_id = [student.id for student in students]

    response = client.patch(f'/api/v1/courses/{course[0].id}/', data={'students': students_id})

    assert response.status_code == expected_status
    data = response.json()
    if response.status_code == 200:
        assert data['students'] == students_id


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    id = course[0].id
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1