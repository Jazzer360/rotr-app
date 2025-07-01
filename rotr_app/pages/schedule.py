import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import apply_start_end


friday = [
    {
        'name': 'MorningBird',
        'day': 'F',
        'time': '5:00pm - 6:00pm',
        'stage': 'Main',
        'bio': """
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
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'morningbird.jpg'),
        'web': 'https://morningbirdsings.com/',
        'fb': 'https://www.facebook.com/robandjill/',
        'insta': '',
        'spotify': '',
        'apple': '',
        'yt': 'https://www.youtube.com/channel/UCfcjI9Hza-HCgZaYT7syl6w',
    },
    {
        'name': 'The Quantum Mechanics',
        'day': 'F',
        'time': '6:30pm - 7:30pm',
        'stage': 'Main',
        'bio': """
            The Quantum Mechanics are an "inter-dimensional jam band" based
            out of Minnesota. This unique group blends elements of rock,
            jazz, and funk with a quirky, psychedelic twist.  Their
            original music explores unconventional themes like subatomic
            particles, parallel dimensions, and alternate realities, all
            delivered with a sense of humor and musical adventurousness.
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'quantummechanics.jpg'),
        'web': 'https://captaingravitone.com/',
        'fb': 'https://www.facebook.com/quantummechanicsband/',
        'insta': 'https://www.instagram.com/thequantummechanics_band/',
        'spotify': '',
        'apple': '',
        'yt': '',
    },
    {
        'name': 'Reed Anderberg',
        'day': 'F',
        'time': '7:30pm - 8:00pm',
        'stage': 'Church',
        'bio': """
            Reed Anderberg is a local musician from Tea, South Dakota.
            """,
        'img': '',
        'fb': '',
        'insta': '',
        'apple': '',
        'yt': '',
    },
    {
        'name': 'Todd Partridge',
        'day': 'F',
        'time': '8:00pm - 9:00pm',
        'stage': 'Main',
        'bio': """
            The Todd show is a foot stompin’, hand clappin’ rock and roll
            gospel, with heartfelt ballads and sing-a-longs.  According to
            “City View” show reviewer Chad Taylor, He is “Part troubadour,
            part tent revival preacher, Partridge holds court over his
            audience, welcoming all to the Tramps roots rock/jam band
            sound with the charisma of a faith healer.”
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'toddpartridge.jpg'),
        'web': 'https://todd-partridge.com/',
        'fb': 'https://www.facebook.com/profile.php?id=100094025644790',
        'insta': 'https://www.instagram.com/todd_partridge/',
        'spotify': 'https://open.spotify.com/artist/3wrOvMs2zdWsqgEpQnnFrj',
        'apple': 'https://music.apple.com/us/artist/todd-partridge/1609807636',
        'yt': '',
    },
    {
        'name': 'Life in Progress',
        'day': 'F',
        'time': '9:00pm - 9:30pm',
        'stage': 'Church',
        'bio': """
            Life in Progress is a local duo composed of Mike & Bailey Hobbs
            from Dunnell, Minnesota who create uplifting lyrical harmonies
            with acoustic guitar and Ukelele. They host an annual music
            festival on their farm called Cornstalk.
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'lifeinprogress.jpg'),
        'web': 'https://cornstalkconvergence.com/',
        'fb': 'https://www.facebook.com/profile.php?id=100063881920787',
        'insta': 'https://www.instagram.com/cornstalkconvergence',
        'spotify': '',
        'apple': '',
        'yt': '',
    },
    {
        'name': 'Saltydog',
        'day': 'F',
        'time': '9:30pm - 11:00pm',
        'stage': 'Main',
        'bio': """
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
        'img': 'https://storage.googleapis.com/rotr-app-assets/saltydog.jpg',
        'web': 'https://saltydogduluth.band/',
        'fb': 'https://www.facebook.com/saltydog.duluth',
        'insta': 'https://www.instagram.com/saltydog.duluth/',
        'spotify': 'https://open.spotify.com/artist/5u7Gz7FFd3fhhN4pk7817j',
        'apple': '',
        'yt': 'https://www.youtube.com/channel/UC1hWJOLqGgTS3zOX8Eqz5vw'
    }
]
saturday = [
    {
        'name': 'Harper & Midwest Kind Sound Journey',
        'day': 'S',
        'time': '1:30pm - 2:30pm',
        'stage': 'Main',
        'bio': """
            Harper & Midwest Kind Sound Journey is a musical project led by
            Australian musician Peter D. Harper. It blends blues, roots,
            and world music influences, often incorporating the didgeridoo,
            an Aboriginal Australian instrument. Their performances offer a
            unique and immersive sound experience, sometimes described as
            "sound baths," that aim to promote relaxation and well-being.
            """,
        'img': 'https://storage.googleapis.com/rotr-app-assets/harper.jpg',
        'web': 'https://harper.biz',
        'fb': 'https://www.facebook.com/HarperandMidwestKind/',
        'insta': 'https://instagram.com/harperandmidwestkind',
        'spotify': 'https://open.spotify.com/artist/0kqjMIDhc7wA1aoJD1aOuY',
        'apple': '',
        'yt': 'https://youtube.com/peterdharper',
    },
    {
        'name': 'Emma Josephine',
        'day': 'S',
        'time': '2:30pm - 3:00pm',
        'stage': 'Church',
        'bio': """
            Emma Josephine is a singer-songwriter based in Mankato,
            Minnesota, who also performs in the Twin Cities area. She is
            known for her folk-inspired sound and soulful storytelling,
            often performing as a solo act with her acoustic guitar.
            Emma Josephine has gained recognition through performances at
            festivals like the Rock Bend Folk Festival and has opened for
            artists such as The Cactus Blossoms and Mary Jane Alm. Her
            songwriting style is described as capturing the lyrical power
            of Brandi Carlile, the folk flair of Emmylou Harris, and the
            rich storytelling of Nanci Griffith. She also has experience
            leading worship in churches.
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'emmajosephine.jpg'),
        'web': 'https://sites.google.com/view/justemmajomusic/home',
        'fb': 'https://www.facebook.com/emma.josephine.252982/',
        'insta': 'https://www.instagram.com/justemmajomusic/',
        'spotify': 'https://open.spotify.com/artist/7kIGLRUGjUCgKJQlHQ8174',
        'apple': 'https://music.apple.com/us/artist/emma-josephine/1645276407',
        'yt': 'https://www.youtube.com/@justemmajomusic',
    },
    {
        'name': 'Janice Gilbert',
        'day': 'S',
        'time': '3:00pm - 4:00pm',
        'stage': 'Main',
        'bio': """
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
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'janicegilbert.jpg'),
        'web': 'https://janicegilbert.com/',
        'fb': 'https://www.facebook.com/janicegilbertmusic',
        'insta': 'https://www.instagram.com/janicegilbert23',
        'spotify': 'https://open.spotify.com/artist/0XMI3C705bdTGHmck6mQ01',
        'apple': 'https://music.apple.com/us/artist/janice-gilbert/295352162',
        'yt': 'https://www.youtube.com/@janicegilbertmusic',
    },
    {
        'name': 'Squid City Slingers',
        'day': 'S',
        'time': '4:30pm - 5:30pm',
        'stage': 'Main',
        'bio': """
            Squid City Slingers are a dynamic trio hailing from the Twin
            Cities, Minnesota, with a strong presence in the Twin Ports
            area as well. They've carved out a niche for themselves with
            their unique blend of folk, bluegrass, and gypsy jazz
            influences. Think lively fiddle tunes, intricate guitar
            picking, and soulful vocals, all wrapped up in a high-energy
            performance style that gets audiences moving. They are known
            for their engaging live shows, often playing breweries, pubs,
            and festivals around the region. If you're looking for a band
            that will bring a fun and eclectic mix of music to your event,
            the Squid City Slingers might be just what you need.
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'squidcityslingers.jpg'),
        'web': '',
        'fb': ('https://www.facebook.com/profile.php'
               '?id=61550201452681&mibextid=avESrC'),
        'insta': 'https://www.instagram.com/squidcityslingers',
        'spotify': '',
        'apple': '',
        'yt': 'https://www.youtube.com/@SquidCitySlingers/videos',
    },
    {
        'name': 'Dan Rodriguez',
        'day': 'S',
        'time': '6:00pm - 7:15pm',
        'stage': 'Main',
        'bio': """
            Dan Rodriguez is a Minneapolis-based singer-songwriter
            originally from Detroit. Known for his soulful voice and
            heartfelt lyrics, he's released several albums and EPs, and has
            even had his music featured in commercials (Miller Lite) and
            tourism campaigns (Explore Minnesota). Dan's a husband and
            father who enjoys the outdoors, good food, and connecting with
            people through his music. He's shared the stage with notable
            artists like The Civil Wars, Andy Grammer, and Eric Hutchinson.
            """,
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'danrodriguez.jpg'),
        'web': 'https://www.danrodriguezmusic.com/',
        'fb': 'https://www.facebook.com/danrodriguezmusic/',
        'insta': 'https://www.instagram.com/danrodriguezmusic',
        'spotify': 'https://open.spotify.com/artist/5T7PSvUO7Sm6AskUrp9iER',
        'apple': 'https://music.apple.com/us/artist/dan-rodriguez/336324136',
        'yt': 'https://www.youtube.com/channel/UCp70GsPgfZUn8IT3zYTITIQ',
    },
    {
        'name': 'Janice Gilbert',
        'day': 'S',
        'time': '7:15pm - 7:45pm',
        'stage': 'Church',
        'bio': """
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
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'janicegilbert.jpg'),
        'web': 'https://janicegilbert.com/',
        'fb': 'https://www.facebook.com/janicegilbertmusic',
        'insta': 'https://www.instagram.com/janicegilbert23',
        'spotify': 'https://open.spotify.com/artist/0XMI3C705bdTGHmck6mQ01',
        'apple': 'https://music.apple.com/us/artist/janice-gilbert/295352162',
        'yt': 'https://www.youtube.com/@janicegilbertmusic',
    },
    {
        'name': 'Joseph Huber',
        'day': 'S',
        'time': '7:45pm - 9:00pm',
        'stage': 'Main',
        'bio': """
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
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'josephhuber.jpg'),
        'web': 'http://www.josephhubermusic.com/',
        'fb': '',
        'insta': 'https://www.instagram.com/josephhubermusic',
        'spotify': 'https://open.spotify.com/artist/2pzKzgyZZdp2u8e8r3T1qa',
        'apple': ('https://music.apple.com/us/artist/'
                  'joseph-huber-band/1743114017'),
        'yt': 'https://www.youtube.com/channel/UCku4bBFeP60zw_CdHkufd6g',
    },
    {
        'name': 'Tim Fast',
        'day': 'S',
        'time': '9:00pm - 9:30pm',
        'stage': 'Church',
        'bio': """
            Tim Fast is an award-winning folk singer-songwriter from
            Minnesota. He's known for his heartfelt lyrics, engaging
            melodies, and intimate performances that connect with audiences
            on a personal level. His music often draws inspiration from the
            landscapes and stories of the Midwest, creating a sense of
            warmth and familiarity. Fast is a skilled guitarist and
            harmonica player, and his music has earned him recognition at
            various festivals and venues. If you're a fan of authentic folk
            music with a focus on storytelling, Tim Fast is definitely
            worth checking out.
            """,
        'img': 'https://storage.googleapis.com/rotr-app-assets/timfast.jpg',
        'web': 'https://timfast.com/',
        'fb': 'https://www.facebook.com/timfastmusic',
        'insta': '',
        'spotify': 'https://open.spotify.com/artist/1ggS81qFjGR5kNQCzk2DHE',
        'apple': '',
        'yt': 'https://youtube.com/@timfastmusic',
    },
    {
        'name': 'Squeaky Feet',
        'day': 'S',
        'time': '9:30pm - 11:00pm',
        'stage': 'Main',
        'bio': """
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
        'img': ('https://storage.googleapis.com/rotr-app-assets/'
                'squeakyfeet.jpg'),
        'web': 'https://www.squeakyfeetmusic.com/',
        'fb': 'https://www.facebook.com/squeakyfeetmusic/',
        'insta': 'https://www.instagram.com/squeakyfeetmusic',
        'spotify': 'https://open.spotify.com/artist/2TX98d6WbDmTYDRVKAb2vF',
        'apple': 'https://music.apple.com/us/artist/squeaky-feet/1501244406',
        'yt': 'https://www.youtube.com/@squeakyfeet6648'
    }
]

apply_start_end(friday)
apply_start_end(saturday)


class ScheduleState(rx.State):
    @rx.event
    def show_toast(self):
        yield NavState.update
        return rx.toast.info(
            'Click a band to learn more about them.',
            duration=5000,
            close_button=True
        )


def on_stage_component(component_function):
    def wrapper(band: dict):
        return rx.cond(
            (band['start'] < NavState.now) & (band['end'] > NavState.now),
            component_function(band),
            rx.fragment()
        )
    return wrapper


@on_stage_component
def time_left_text(band: dict) -> rx.Component:
    return rx.text(
            (band['end'] - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
    )


@on_stage_component
def badge(band: dict) -> rx.Component:
    return rx.badge('On Stage', align_self='flex-end')


@on_stage_component
def progress(band: dict) -> rx.Component:
    return rx.progress(
        value=((NavState.now - band['start']) /
               (band['end'] - band['start']) * 100),
        margin_top='8px'
    )


def band_card(band: dict) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.text(
                band['stage'],
                size='1',
                writing_mode='vertical-lr',
                transform='scale(-1)'
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        band['name'],
                        font_weight=rx.cond(
                            band['stage'] == 'Main', 'bold', 'normal'
                        )
                    ),
                    rx.spacer(),
                    badge(band),
                    width='100%'
                ),
                rx.hstack(
                    rx.text(band['time']),
                    time_left_text(band),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress(band),
        color=rx.cond(band['end'] < NavState.now, 'gray', ''),
        margin_left=rx.cond(band['stage'] == 'Main', '0px', '20px')
    )


def link(band: dict, attr: str, icontag: str, text: str) -> rx.Component:
    return rx.cond(
        band.get(attr),
        rx.link(
            rx.hstack(
                rx.icon(tag=icontag),
                rx.text(text)
            ),
            href=band.get(attr)
        )
    )


def links(band: dict) -> rx.Component:
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


def band_entry(band: dict) -> rx.Component:
    return rx.container(
        rx.dialog.root(
            rx.dialog.trigger(
                band_card(band)
            ),
            rx.dialog.content(
                rx.hstack(
                    rx.dialog.title(band['name'], padding_top='8px'),
                    rx.spacer(),
                    rx.dialog.close(rx.icon('x'))
                ),
                rx.cond(band.get('img'), rx.image(src=band.get('img'))),
                rx.dialog.description(band.get('bio'), margin='12px 0px'),
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
            [band_entry(band) for band in friday],
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            [band_entry(band) for band in saturday],
            width='100%'
        ),
        width='100%',
        align='center'
    )
