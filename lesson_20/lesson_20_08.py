class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


def is_instance(obj_list, cls_list):
    for obj in obj_list:
        for cls in cls_list:
            print(isinstance(obj, cls), end='\t')
        print()


if __name__ == '__main__':
    vehicle_obj = Vehicle()
    land_vehicle_obj = LandVehicle()
    tracked_vehicle_obj = TrackedVehicle()
    my_obj_list = [vehicle_obj, land_vehicle_obj, tracked_vehicle_obj]
    my_cls_list = [Vehicle, LandVehicle, TrackedVehicle]
    is_instance(obj_list=my_obj_list, cls_list=my_cls_list)
