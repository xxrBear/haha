from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse


def test_rawqueryset(request):
    sql = 'select * from user;'

    raw_queryset = RawQuerySet(raw_query=sql, using='default')
    print(raw_queryset.model_fields.get('id'))

    return HttpResponse('成功')
