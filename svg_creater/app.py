import svgwrite


def basic_shapes(name):
    dwg = svgwrite.Drawing(
        filename=name,
        debug=True,
        viewBox='0 0 100 100',
        x=0,
        y=0,
        style="enable-background:new 0 0 100 100;")

    # Шляпа и тело.
    dwg.add(svgwrite.shapes.Polygon(
        points=[(62, 47.2), (24.7, 5.8), (22.6, 8.1), (57.9, 47.2)],
        fill='#CBA349'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(55.8, 47.2), (21.6, 9.2), (19.5, 11.6), (51.6, 47.2)],
        fill='#CBA349'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(74.5, 47.2), (70.4, 47.2), (32, 4.6), (34.1, 2.3)],
        fill='#13007C'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(28.9, 8.1), (64.1, 47.2), (68.3, 47.2), (31, 5.8)],
        fill='#CBA349'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(28.5, 47.2), (49.5, 47.2), (39, 35.5)],
        fill='#008837'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(9.7, 47.2), (13.9, 47.2), (21.8, 38.5), (17.6, 38.5)],
        fill='#0E0E6B'))
    dwg.add(svgwrite.shapes.Polygon(
        points=[(3.5, 47.2), (7.6, 47.2), (15.5, 38.5), (11.4, 38.5)],
        fill='#0E0E6B'))

    dwg.add(svgwrite.shapes.Polygon(
        points=[(22.2, 47.2), (26.4, 47.2), (32.4, 40.5), (38, 34.4),
                (35.9, 32.1)], fill='#CBA349'))

    # Лицо.
    path_data = """M16,47.2 h4.2 l14.7,-16.3 C30.4,26,26,21.1,21.6,16.2 l-3.2,
    3.6,1,1.2 -4.1,4.6 -0.8,0.9 -0.2,0.2 1.5,1.7 -1,1.2 1.3,1.5 -1.3,1.4 1,
    1.1 -3,3.4 h12.5 L16,47.2 z m6.2,0 h4.2 l6,-6.7 5.6,-6.1 -2.1,-2.3 z"""

    path = dwg.path(d=path_data, fill='#CBA349')
    dwg.add(path)

    dwg.save()

    return name


def create_html_page(image_path):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SVG Image</title>
    </head>
    <body>
        <h1>SVG Image</h1>
        <img src="{image_path}" alt="SVG Image">
    </body>
    </html>
    """

    with open("index.html", "w") as html_file:
        html_file.write(html_content)


if __name__ == '__main__':
    image_path = basic_shapes('src/salavat.svg')
    create_html_page(image_path=image_path)
