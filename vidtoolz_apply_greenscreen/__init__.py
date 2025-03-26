import vidtoolz
import os
from vidtoolz_apply_greenscreen.apply_greenscreen import overlay_greenscreen, write_clip


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_trim.mp4")


def create_parser(subparser):
    parser = subparser.add_parser(
        "greenscreen", description="Apply greenscreen video on top of a video"
    )
    # Add subprser arguments here.
    parser.add_argument("main_video", help="Path to the main video file.")
    parser.add_argument(
        "greenscreen_video", help="Path to the green screen video file."
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output video file name (default: output.mp4)",
    )
    parser.add_argument(
        "-p",
        "--position",
        choices=[
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "center",
            "bottom",
        ],
        default="bottom",
        help="Position of the green screen video (default: bottom)",
    )
    parser.add_argument(
        "-s",
        "--start-time",
        type=int,
        default=1,
        help="Start time in seconds of the overlay. Default 1",
    )

    return parser


class ViztoolzPlugin:
    """Apply greenscreen video on top of a video"""

    __name__ = "greenscreen"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):

        output = determine_output_path(args.main_video, args.output)
        clip, fps = overlay_greenscreen(
            args.main_video, args.greenscreen_video, args.position, args.start_time
        )
        write_clip(clip, output, fps)
        print(f"{output} written")

    def hello(self, args):
        # this routine will be called when "vidtoolz "greenscreen is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


greenscreen_plugin = ViztoolzPlugin()
