import pytest

from rest_framework.test import APIClient

from students.models import Course, Student
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_single_course(client, courses_factory):
    #Arange
    quantity = 1
    courses = courses_factory(_quantity=quantity)

    #Act
    response = client.get('/api/v1/courses/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_get_course_list(client, courses_factory):
    #Arange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    #Act
    response = client.get('/api/v1/courses/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_create_single_course(client):
    #Arange
    count = Course.objects.count()

    #Act
    response = client.post('/api/v1/courses/', data={'name': 'C++', "students": []})

    #Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    data = response.json()
    assert data['name'] == 'C++'

@pytest.mark.django_db
def test_create_many_courses(client, courses_factory):
    #Arange
    count = Course.objects.count()
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    #Act
    response = client.get('/api/v1/courses/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert Course.objects.count() == count + quantity
    
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name

@pytest.mark.django_db
def test_filter_id_courses(client, courses_factory):
    #Arange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    for course in courses:
        url = '/api/v1/courses/?id=' + str(course.id)
        #Act
        response = client.get(url)
    
        #Assert
        assert response.status_code == 200
        data = response.json()
        assert data[0]['id'] == course.id

@pytest.mark.django_db
def test_filter_name_courses(client, courses_factory):
    #Arange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    for course in courses:
        url = '/api/v1/courses/?name=' + course.name
        #Act
        response = client.get(url)
    
        #Assert
        assert response.status_code == 200
        data = response.json()
        assert data[0]['name'] == course.name

@pytest.mark.django_db
def test_update_course(client, courses_factory):
    #Arange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    for course in courses:
       #Act
        url = '/api/v1/courses/' + str(course.id) + '/'
        response = client.patch(url, data={'name': 'C++'})
    
        #Assert
        assert response.status_code == 200
        data = response.json()
        assert data['name'] == 'C++'

@pytest.mark.django_db
def test_delete_courses(client, courses_factory):
    #Arange
    quantity = 10
    courses = courses_factory(_quantity=quantity)

    for course in courses:
       #Act
        url = '/api/v1/courses/' + str(course.id) + '/'
        response = client.delete(url)
    
        #Assert
        assert response.status_code == 204
