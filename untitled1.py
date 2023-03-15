import os
import argparse
import matplotlib.pyplot as plt
import mvn
from load_mvnx import load_mvnx
from tqdm import tqdm


def mvnx2dict(mvnx_file):
    # No estoy segura de si footContact y frame sirven de algo. 
    myDict = {
        'segmentData': {},
        'sensorData': {},
        'jointData': {},
        'ergoJointData': {},
        'footContact': {},
        'frame': {
            'time': [],
            'type': [],
            'globalPosition': [],
            'centerOfMass': []
        }
    }

    for i in tqdm(range(23)):
        segment_name = mvnx_file.segment_name_from_index(i)
        print(i)
        myDict['segmentData'][segment_name] = {
            'orientation': mvnx_file.get_segment_ori(i),
            'position': mvnx_file.get_segment_pos(i),
            'velocity': mvnx_file.get_segment_vel(i),
            'acceleration': mvnx_file.get_segment_acc(i),
            'angularVelocity': mvnx_file.get_segment_angular_vel(i),
            'angularAcceleration': mvnx_file.get_segment_angular_acc(i)
        }

    number_of_activated_sensors = mvnx_file.sensor_count
    sensorNames = mvnx_file.file_data['sensors']['names']
    segmentNames = mvnx_file.file_data['segments']['names']
    for i in tqdm(range(len(segmentNames))):

        sensor = segmentNames[i]
        if sensor in sensorNames:
            print(i)
            myDict['sensorData'][sensor] = {
                'sensorFreeAcceleration': mvnx_file.get_sensor_free_acc(i),
                'sensorMagneticField': mvnx_file.get_segment_pos(i),  # Al parecer no existe la funcion que lo obtinene
                'sensorOrientation': mvnx_file.get_sensor_ori(i),
            }

    for i in tqdm(range(len(segmentNames) - 1)):
        print(i)
        j = i + 1
        joint = mvnx_file.point_name_from_indices(j, 0)

        myDict['jointData'][joint] = {
            'jointAngle': mvnx_file.get_joint_angle(i),
            'jointAngleXZY': mvnx_file.get_joint_angle_xzy(i)
        }

    ergoJointNames = ['T8_Head', 'T8_LeftUpperArm', 'T8_RightUpperArm', 'Pelvis_T8', 'Vertical_Pelvis', 'Vertical_T8']
    for i in tqdm(range(len(ergoJointNames))):
        print(i)
        ergoJoint = ergoJointNames[i]
        myDict['ergoJointData'][ergoJoint] = {
            'jointAngleErgo': mvnx_file.get_ergo_joint_angle(i),
            'jointAngleErgoXZY': mvnx_file.get_joint_angle_xzy(i)  # No existe funcion
        }


    #with open('P6_medium_round.txt', 'w') as file:

        # Loop over the dictionary and write each key-value pair to the file
        #for key, value in myDict.items():
            #file.write(f'{key}: {value}\n')

    print('Almost there')
    return myDict




