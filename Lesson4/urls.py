from datetime import datetime

from views import Index, About, StudyPrograms, CoursesList, NotFound404, CreateCourse, CreateCategory, CategoryList, CopyCourse


# Front controllers
def time_front(request):
    request['time'] = datetime.now().time().strftime("%H:%M")


def date_front(request):
    request['year'] = datetime.now().today().year


def other_front(request):
    request['key'] = 'key'


routes = {
    '/': Index(),
    '/about/': About(),
    '/404': NotFound404(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}

fronts = [time_front, date_front, other_front]
