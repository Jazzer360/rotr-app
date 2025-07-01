import reflex as rx


def footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            "Privacy Notice",
            href='/privacy.html'
        )
    )
