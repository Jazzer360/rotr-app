"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

app = rx.App(
    head_components=[
        rx.script(
            """
            (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','GTM-KK4RPDQN');
            """)
    ],
    theme=rx.theme(appearance='dark')
)
