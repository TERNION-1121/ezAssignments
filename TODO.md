# TODOS

- Image functionality

  - At the end of each question's content, in the final line `[<image_name>.<exension>]` should be added.

  - Process this while using the `from_list_contents()` method.

  - Possibly a utility function would parse this image name.

  - An `image` attribute for each question; defaults to **None**

  - While writing each question to the doc,
maybe have a method to write the image pointed by the image attr of the question object, if not **None**

  - Image assets should be stored in the `images` subdirectory of the directory pointed by the `dir_path` command line argument.

<br>

- Add new question type: Case Studies