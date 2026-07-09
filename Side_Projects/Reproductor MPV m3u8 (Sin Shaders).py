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

    # MPV instalado normalmente
    if shutil.which("mpv"):
        return ["mpv"]


    # MPV Flatpak (Bazzite)
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
        print()
        print(
            "Instala con:"
        )
        print(
            "flatpak install flathub io.mpv.Mpv"
        )

        return



    print(
        "✔ MPV encontrado:",
        " ".join(mpv)
    )


    print(
        "✔ Anime4K activo: No"
    )

    print(
        "✔ Shaders enviados: 0"
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
        # BUFFER HLS
        # ==========================

        "--cache=yes",

        # Lectura anticipada
        "--demuxer-readahead-secs=120",

        # Máximo de caché permitido
        "--demuxer-max-bytes=500M",

        # Evitar pausa automática del buffer
        "--cache-pause=no",



        # ==========================
        # HLS / RED
        # ==========================

        "--hls-bitrate=max",

        "--network-timeout=30",

        "--stream-buffer-size=64MiB",

        "--prefetch-playlist=yes",



        # ==========================
        # GPU / VIDEO
        # ==========================

        "--vo=gpu-next",

        "--gpu-api=vulkan",

        "--hwdec=auto-safe",



        # ==========================
        # CALIDAD
        # ==========================

        "--video-sync=display-resample",

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



    print()
    print(
        "Abriendo MPV..."
    )
    print()


    subprocess.run(cmd)



if __name__ == "__main__":
    main()