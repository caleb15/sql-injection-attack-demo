from django.db import connection
from django.shortcuts import render
from django.views import View


class SearchView(View):
    template_name = 'items.html'

    def get(self, request, *args, **kwargs):
        q = (request.GET.get('q') or '').strip()

        sql = """
        SELECT name
        FROM orders_item
        """

        if q:
            sql += f"WHERE name LIKE '%{q}%'"

        print(sql)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        rows = [row[0] for row in rows]

        context = {
            'rows': rows,
        }

        return render(request, self.template_name, context)

