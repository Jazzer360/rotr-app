from datetime import datetime
from typing import Type, TypeVar

import pytz

import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import production, get_start_end

T = TypeVar('T', bound='BandInfo')


class BandInfo(rx.Base):
    name: str
    time: str
    stage: str
    start: int
    end: int
    img: str = None
    bio: str = None
    web: str = None
    fb: str = None
    insta: str = None
    spotify: str = None
    apple: str = None
    yt: str = None

    @classmethod
    def create(cls: Type[T], *, name: str, day: str, time: str, stage: str,
               **kwargs: dict[str, str]) -> T:
        if production():
            fri = '2025-07-11'
            sat = '2025-07-12'
        else:
            fri = datetime.now(
                pytz.timezone('America/Chicago')).strftime('%Y-%m-%d')
            sat = fri
        date = fri if day == 'F' else sat
        return BandInfo(
            name=name,
            time=time,
            stage=stage,
            **(kwargs | get_start_end(date, time))
        )


class ScheduleState(rx.State):
    friday: list[BandInfo] = [
        BandInfo.create(
            name='MorningBird',
            day='F',
            time='5:00pm - 6:00pm',
            stage='Main',
            bio="""
                MorningBird is an acoustic trio from northern Minnesota that
                blends folk, Americana, and bluegrass influences. Originally
                starting as a duo in 2020 with Rob Wheeler and Jill Burkes,
                they added upright bassist Josh Palmi in 2023.  Their music
                features strong vocal harmonies, intricate string arrangements,
                and a focus on storytelling.  They perform both original songs
                and unique covers, often drawing inspiration from traditional
                folk music and the natural beauty of their surroundings.
                Their latest album, "Echoes in the Meadow," showcases their
                evolving sound and commitment to crafting honest, heartfelt
                music.
                """,
            img='https://storage.googleapis.com/rotr-app-assets/morningbird.jpg',
            web='https://morningbirdsings.com/',
            fb='https://www.facebook.com/robandjill/',
            insta='',
            spotify='',
            apple='',
            yt='https://www.youtube.com/channel/UCfcjI9Hza-HCgZaYT7syl6w'),
        BandInfo.create(
            name='',
            day='F',
            time='6:00pm - 6:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='The Quantum Mechanics',
            day='F',
            time='6:30pm - 7:30pm',
            stage='Main',
            bio="""
                The Quantum Mechanics are an "inter-dimensional jam band" based
                out of Minnesota. This unique group blends elements of rock,
                jazz, and funk with a quirky, psychedelic twist.  Their
                original music explores unconventional themes like subatomic
                particles, parallel dimensions, and alternate realities, all
                delivered with a sense of humor and musical adventurousness.
                """,
            img='https://storage.googleapis.com/rotr-app-assets/quantummechanics.jpg',
            web='https://captaingravitone.com/',
            fb='https://www.facebook.com/quantummechanicsband/',
            insta='https://www.instagram.com/thequantummechanics_band/',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='7:30pm - 8:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            fb='',
            insta='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Todd Partridge',
            day='F',
            time='8:00pm - 9:00pm',
            stage='Main',
            bio="""
                The Todd show is a foot stompin’, hand clappin’ rock and roll
                gospel, with heartfelt ballads and sing-a-longs.  According to
                “City View” show reviewer Chad Taylor, He is “Part troubadour,
                part tent revival preacher, Partridge holds court over his
                audience, welcoming all to the Tramps roots rock/jam band
                sound with the charisma of a faith healer.”
                """,
            img='https://storage.googleapis.com/rotr-app-assets/toddpartridge.jpg',
            web='https://todd-partridge.com/',
            fb='https://www.facebook.com/profile.php?id=100094025644790',
            insta='https://www.instagram.com/todd_partridge/',
            spotify='https://open.spotify.com/artist/3wrOvMs2zdWsqgEpQnnFrj',
            apple='https://music.apple.com/us/artist/todd-partridge/1609807636',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Saltydog',
            day='F',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                Saltydog is a high-energy funk jam band based in Duluth,
                Minnesota.  Known for their lively improvisations and
                infectious grooves, they create a dynamic blend of funk, rock,
                and soul. The band features Jacob Mahon on guitar and vocals,
                Owen Mahon on drums and vocals, Calzone on bass, Sam on guitar,
                Lefty on auxiliary percussion and vocals, and Gavin St. Clair
                on keys and vocals.  They released their second studio album in
                June 2024 and are known for their "High Key Mondays" residency
                at Bent Paddle Brewing in Duluth. Saltydog is a rising force in
                the Midwest music scene, captivating audiences with their
                unique sound and electrifying live performances.

                """,
            img='https://storage.googleapis.com/rotr-app-assets/saltydog.jpg',
            web='https://saltydogduluth.band/',
            fb='https://www.facebook.com/saltydog.duluth',
            insta='https://www.instagram.com/saltydog.duluth/',
            spotify='https://open.spotify.com/artist/5u7Gz7FFd3fhhN4pk7817j',
            apple='',
            yt='https://www.youtube.com/channel/UC1hWJOLqGgTS3zOX8Eqz5vw')
    ]
    saturday: list[BandInfo] = [
        BandInfo.create(
            name='',
            day='S',
            time='1:30pm - 2:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='2:30pm - 3:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Janice Gilbert',
            day='S',
            time='3:00pm - 4:00pm',
            stage='Main',
            bio="""
                Janice Gilbert is a country singer-songwriter with a
                down-to-earth style rooted in her South Dakota upbringing.
                Her music blends contemporary country with touches of folk and
                Americana, reflecting her rural roots and personal experiences.
                Gilbert's songs often touch on themes of family, faith, and
                life on the farm, with heartfelt lyrics and a warm vocal
                delivery. She has earned recognition for her songwriting,
                winning contests and placing songs on TV shows like "White Wall
                Sessions." Although she spent time honing her craft in
                Nashville, Gilbert now performs throughout the Midwest, sharing
                her genuine stories and connecting with audiences through her
                music.
                """,
            img='https://storage.googleapis.com/rotr-app-assets/janicegilbert.jpg',
            web='https://janicegilbert.com/',
            fb='https://www.facebook.com/janicegilbertmusic',
            insta='https://www.instagram.com/janicegilbert23',
            spotify='https://open.spotify.com/artist/0XMI3C705bdTGHmck6mQ01',
            apple='https://music.apple.com/us/artist/janice-gilbert/295352162',
            yt='https://www.youtube.com/@janicegilbertmusic'),
        BandInfo.create(
            name='',
            day='S',
            time='4:00pm - 4:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='4:30pm - 5:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='5:30pm - 6:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Dan Rodriguez',
            day='S',
            time='6:00pm - 7:15pm',
            stage='Main',
            bio="""
                Music is my trade & performing it for people is my passion.
                When I’m not in my studio writing songs and cutting records, or
                on the road playing shows, I’m usually tending to our backyard
                chickens, eating fresh veggies from my wife’s huge garden,
                making syrup from our city maples, or doing one of my many
                outdoor hobbies.
                """,
            img='https://storage.googleapis.com/rotr-app-assets/danrodriguez.jpg',
            web='https://www.danrodriguezmusic.com/',
            fb='https://www.facebook.com/danrodriguezmusic/',
            insta='https://www.instagram.com/danrodriguezmusic',
            spotify='https://open.spotify.com/artist/5T7PSvUO7Sm6AskUrp9iER',
            apple='https://music.apple.com/us/artist/dan-rodr%C3%ADguez/1453645877',
            yt='https://www.youtube.com/channel/UCp70GsPgfZUn8IT3zYTITIQ'),
        BandInfo.create(
            name='',
            day='S',
            time='7:15pm - 7:45pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Joseph Huber',
            day='S',
            time='7:45pm - 9:00pm',
            stage='Main',
            bio="""
                Joseph Huber is a Milwaukee-based musician who blends elements
                of bluegrass, folk, and country into his own unique sound.
                Often performing solo with just his voice and banjo, or
                sometimes accompanied by a band, his music evokes a raw and
                timeless quality.  His songs often explore themes of love,
                loss, hardship, and the beauty of the natural world, drawing
                inspiration from his own life experiences and the landscapes
                of the Midwest. With introspective lyrics and a soulful
                delivery, Huber's music resonates with listeners on an
                emotional level, offering a glimpse into the heart of
                Americana.

                """,
            img='https://storage.googleapis.com/rotr-app-assets/josephhuber.jpg',
            web='http://www.josephhubermusic.com/',
            fb='https://www.facebook.com/josephhubermusicprofile/',
            insta='https://www.instagram.com/josephhubermusic',
            spotify='https://open.spotify.com/artist/2pzKzgyZZdp2u8e8r3T1qa',
            apple='https://music.apple.com/us/artist/joseph-huber-band/1743114017',
            yt='https://www.youtube.com/channel/UCku4bBFeP60zw_CdHkufd6g'),
        BandInfo.create(
            name='',
            day='S',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Squeaky Feet',
            day='S',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                Squeaky Feet is a modern jam band from Denver, Colorado known
                for their unique blend of progressive rock and jazz fusion.
                This quintet delivers high-energy performances filled with
                intricate jams, soaring solos, and complex compositions.
                Influenced by 70s prog rock giants, they create a captivating
                sonic experience that pushes the boundaries of improvisation
                while maintaining a strong sense of groove. Their debut album,
                "Cause For Alarm," showcases their impressive musicianship and
                innovative approach to music. Squeaky Feet is quickly gaining
                recognition for their electrifying live shows and their ability
                to take listeners on a mind-bending journey through sound.
                """,
            img='https://storage.googleapis.com/rotr-app-assets/squeakyfeet.jpg',
            web='https://www.squeakyfeetmusic.com/',
            fb='https://www.facebook.com/squeakyfeetmusic/',
            insta='https://www.instagram.com/squeakyfeetmusic',
            spotify='https://open.spotify.com/artist/2TX98d6WbDmTYDRVKAb2vF',
            apple='https://music.apple.com/us/artist/squeaky-feet/1501244406',
            yt='https://www.youtube.com/@squeakyfeet6648')
    ]

    def show_toast(self):
        yield NavState.update
        return rx.toast.info(
            'Click a band to learn more about them.',
            duration=5000,
            close_button=True
        )


def on_stage_component(component_function):
    def wrapper(band: BandInfo):
        return rx.cond(
            (band.start < NavState.now) & (band.end > NavState.now),
            component_function(band),
            rx.fragment()
        )
    return wrapper


@on_stage_component
def time_left_text(band: BandInfo) -> rx.Component:
    return rx.text(
            (band.end - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
    )


@on_stage_component
def badge(band: BandInfo) -> rx.Component:
    return rx.badge('On Stage', align_self='flex-end')


@on_stage_component
def progress(band: BandInfo) -> rx.Component:
    return rx.progress(
        value=((NavState.now - band.start) / (band.end - band.start) * 100),
        margin_top='8px'
    )


def band_card(band: BandInfo) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.text(
                band.stage,
                size='1',
                writing_mode='vertical-lr',
                transform='scale(-1)'
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(band.name),
                    rx.spacer(),
                    badge(band),
                    width='100%'
                ),
                rx.hstack(
                    rx.text(band.time),
                    time_left_text(band),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress(band),
        color=rx.cond(band.end < NavState.now, 'gray', '')
    )


def link(band: BandInfo, attr: str, icontag: str, text: str) -> rx.Component:
    return rx.cond(
        getattr(band, attr, None),
        rx.link(
            rx.hstack(
                rx.icon(tag=icontag),
                rx.text(text)
            ),
            href=getattr(band, attr)
        )
    )


def links(band: BandInfo) -> rx.Component:
    return rx.flex(
        link(band, 'web', 'globe', 'Website'),
        link(band, 'fb', 'facebook', 'Facebook'),
        link(band, 'insta', 'instagram', 'Instagram'),
        link(band, 'spotify', 'audio-lines', 'Spotify'),
        link(band, 'apple', 'apple', 'iTunes'),
        link(band, 'yt', 'youtube', 'YouTube'),
        wrap='wrap',
        spacing='4'
    )


def band_entry(band: BandInfo) -> rx.Component:
    return rx.container(
        rx.dialog.root(
            rx.dialog.trigger(
                band_card(band)
            ),
            rx.dialog.content(
                rx.hstack(
                    rx.dialog.title(band.name, padding_top='8px'),
                    rx.spacer(),
                    rx.dialog.close(rx.icon('x'))
                ),
                rx.cond(band.img, rx.image(src=band.img)),
                rx.dialog.description(band.bio, margin='12px 0px'),
                links(band),
                rx.dialog.close(
                    rx.button('Close', margin_top='24px')
                )
            )
        ),
        size='1',
        padding='8px'
    )


@rx.page(
    route='/',
    title='Live Schedule',
    on_load=ScheduleState.show_toast)
@template
def schedule() -> rx.Component:
    return rx.vstack(
        rx.heading('Friday'),
        rx.box(
            rx.foreach(ScheduleState.friday, band_entry),
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            rx.foreach(ScheduleState.saturday, band_entry),
            width='100%'
        ),
        width='100%',
        align='center'
    )
