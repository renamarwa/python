import graphics.rectangle
import graphics.circle
import graphics.threeDgraphics.cuboid as cuboid
import graphics.threeDgraphics.sphere as sphere

print("Rectangle Area:", graphics.rectangle.area(10, 5))
print("Rectangle Perimeter:", graphics.rectangle.perimeter(10, 5))
print("Circle Area:", graphics.circle.area(7))
print("Circle Perimeter:", graphics.circle.perimeter(7))
print("Cuboid Surface Area:", cuboid.surface_area(4, 5, 6))
print("Cuboid Volume:", cuboid.volume(4, 5, 6))
print("Sphere Surface Area:", sphere.surface_area(3))
print("Sphere Volume:", sphere.volume(3))
