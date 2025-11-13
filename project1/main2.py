from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.threeDgraphics.cuboid import surface_area as cuboid_surface_area, volume as cuboid_volume
from graphics.threeDgraphics.sphere import surface_area as sphere_surface_area, volume as sphere_volume

print("Rectangle Area:", rect_area(10, 5))
print("Rectangle Perimeter:", rect_perimeter(10, 5))
print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_perimeter(7))
print("Cuboid Surface Area:", cuboid_surface_area(4, 5, 6))
print("Cuboid Volume:", cuboid_volume(4, 5, 6))
print("Sphere Surface Area:", sphere_surface_area(3))
print("Sphere Volume:", sphere_volume(3))
