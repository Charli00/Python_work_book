'''An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.'''
import constant

user_input_widgets=int(input("Enter the widgets weight: "))

user_input_gizmo=int(input("Enter the gizmo weights: "))

Weight_widgets=user_input_widgets*constant.wedgets

gizmo_weigth=user_input_gizmo*constant.gizmos

print("Total weight of the order: {}".format(Weight_widgets+gizmo_weigth),sep=",")