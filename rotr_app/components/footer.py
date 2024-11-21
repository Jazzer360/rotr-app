import reflex as rx


def footer():
    return rx.hstack(
        rx.link(
            "Privacy Notice",
            href='/privacy.html'
        )
    )
