"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

app = rx.App(
    head_components=[
        rx.el.script(
            src='https://www.googletagmanager.com/gtag/js?id=G-V97V3QX6KQ',
            async_=True
        ),
        rx.el.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag(`js`, new Date()); gtag(`config`, `G-V97V3QX6KQ`);
            """            
        )
    ]
)
