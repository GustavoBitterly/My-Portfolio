#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path


REFERER = "https://jkanime.net/"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36"
)

HISTORY_FILE = Path.home() / ".mpv_stream_history"


def get_mpv_command():

    if shutil.which("mpv"):
        return ["mpv"]


    if shutil.which("flatpak"):

        result = subprocess.run(
            [
                "flatpak",
                "info",
                "io.mpv.Mpv"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        if result.returncode == 0:

            return [
                "flatpak",
                "run",
                "io.mpv.Mpv"
            ]


    return None



def get_anime4k_shaders():

    shader_dir = (
        Path.home()
        / ".config/mpv/shaders"
    )


    if not shader_dir.exists():
        return None


    shaders = list(
        shader_dir.glob("*.glsl")
    )


    if shaders:
        return shaders


    return None



def save_history(url):

    try:

        with open(
            HISTORY_FILE,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(url + "\n")

    except Exception:
        pass



def show_history():

    if not HISTORY_FILE.exists():
        return


    lines = HISTORY_FILE.read_text(
        encoding="utf-8"
    ).splitlines()


    if lines:

        print("\nÚltimos streams:\n")

        for i, url in enumerate(
            lines[-5:],
            1
        ):

            print(
                f"{i}. {url[:80]}..."
            )

        print()



def main():

    mpv = get_mpv_command()


    if mpv is None:

        print("❌ MPV no encontrado")
        print(
            "Instala:"
        )
        print(
            "flatpak install flathub io.mpv.Mpv"
        )

        return



    print(
        "✔ MPV encontrado:",
        " ".join(mpv)
    )


    show_history()



    url = input(
        "\nPega la URL .m3u8:\n> "
    ).strip()


    if not url.startswith("http"):

        print(
            "❌ URL inválida"
        )

        return



    save_history(url)



    cmd = mpv + [


        # ==========================
        # BUFFER HLS EQUILIBRADO
        # ==========================

        "--cache=yes",

        # Mantener anticipación razonable
        "--demuxer-readahead-secs=120",

        # Máximo 500 MB
        "--demuxer-max-bytes=500M",

        # Evitar pausas automáticas
        "--cache-pause=no",



        # ==========================
        # HLS / RED
        # ==========================

        "--hls-bitrate=max",

        "--prefetch-playlist=yes",

        "--network-timeout=30",

        "--stream-buffer-size=64MiB",



        # ==========================
        # GPU / VIDEO
        # ==========================

        "--vo=gpu-next",

        "--gpu-api=vulkan",

        "--hwdec=auto-safe",



        # ==========================
        # CALIDAD DE IMAGEN
        # ==========================

        "--video-sync=display-resample",

        "--interpolation=yes",

        "--tscale=oversample",

        "--scale=ewa_lanczos",

        "--cscale=ewa_lanczos",



        # ==========================
        # HEADERS
        # ==========================

        f"--http-header-fields=Referer: {REFERER}",

        f"--user-agent={USER_AGENT}",



        # ==========================
        # INTERFAZ
        # ==========================

        "--osd-level=1",


        url
    ]



    # ==========================
    # Anime4K
    # ==========================

    shaders = get_anime4k_shaders()



    if shaders:

        print()
        print(
            "✔ Anime4K activo: Sí"
        )

        print(
            f"✔ Shaders detectados: {len(shaders)}"
        )

        print(
            f"✔ Shaders enviados a MPV: {len(shaders)}"
        )

        print()


        for shader in shaders:

            cmd.insert(
                -1,
                f"--glsl-shaders={shader}"
            )


    else:

        print()
        print(
            "✔ Anime4K activo: No"
        )

        print(
            "✔ Shaders detectados: 0"
        )

        print(
            "✔ Shaders enviados a MPV: 0"
        )

        print()



    print(
        "Abriendo MPV..."
    )

    print()



    subprocess.run(cmd)



if __name__ == "__main__":
    main()