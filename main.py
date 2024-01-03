import bpy
import random

# ! This script is made to modifie player models with bones that are named correctly with the names in the list : Bone_Group, Mixamo's player models, it might not work on other player models !

# Set the alteration, the higher the value gets, the more the player mesh will be alterate
alteration = 3 # You can change the number but 3 is the best (for me)

# Get the armature object
character_name = "Armature"
character = bpy.data.objects[character_name]

# Get all the bones in the armature
all_bones = character.pose.bones

# Set the bone group for random selection
Bone_Group = ["Arm.L", "Arm.R", "ForeArm.L", "ForeArm.R", "Hand.L", "Hand.R", "Head", "Spine", "Chest", "Neck"]

# Get all the bones from the specified bone group
selected_bones = [bone for bone in all_bones if any(group in bone.name for group in Bone_Group)]

# Set the minimum and maximum length variations
min_length_variation = 0.6  # Minimum length variation as a scale factor
max_length_variation = 1.4  # Maximum length variation as a scale factor

# Set the minimum and maximum width variations
min_width_variation = 0.6  # Minimum width variation as a scale factor
max_width_variation = 1.4  # Maximum width variation as a scale factor


for i in range(alteration):
    # Select a random bone from the armature
    bone = random.choice(selected_bones)

    # Get the current bone length and width
    current_length = bone.length
    current_width = bone.scale[0]

    # Generate random variations for length and width
    length_variation = random.uniform(min_length_variation, max_length_variation)
    width_variation = random.uniform(min_width_variation, max_width_variation)

    # Calculate the new bone length and width
    new_length = current_length * length_variation
    new_width = current_width * width_variation

    # Apply the changes to the bone scale
    bone.scale.y *= new_length / current_length
    bone.scale.x *= new_width / current_width

    # Apply the bone scale to the mesh
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    character.select_set(True)
    bpy.context.view_layer.objects.active = character
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.mode_set(mode='POSE')
