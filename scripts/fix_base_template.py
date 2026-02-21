from pathlib import Path
p = Path(r"c:\Users\Admin\API_store\templates\base.html")
content = p.read_text(encoding='utf-8')
# Build corrected template
corrected = """<!DOCTYPE html>
{% load static %}
<html>
<head>
       <title>{% block title %}{% endblock  %}</title>
      <link rel="stylesheet" href="{% static 'assets/style.css' %}">


</head>
<body>
   <main>
         {% block content %}{% endblock %}
   </main>
</body>
</html>
"""
p.write_text(corrected, encoding='utf-8')
print('WROTE', p)
