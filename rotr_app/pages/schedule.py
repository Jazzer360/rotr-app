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
            fri = '2024-07-12'
            sat = '2024-07-13'
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
            name='The MilBillies',
            day='F',
            time='5:00pm - 6:00pm',
            stage='Main',
            bio="""
                WAMI nominated New Artist of the Year (2020), The MilBillies
                are a 5-piece string band that trades vocals like a fifth of
                bourbon and solos like a bull on a rope, slinging high-energy
                bluegrass stripped raw with Americana grit.
                """,
            img='https://i.scdn.co/image/ab6761670000ecd4a23b5e7395f14d5132c0fcdd',
            web='https://themilbillies.com/',
            fb='https://www.facebook.com/TheMilBillies/',
            insta='https://www.instagram.com/milbillies/',
            spotify='https://open.spotify.com/artist/2wbuJcfeMTnL8sGXLS84Nd?si=OcNMYDFISuaqUGFTbE2ykw',
            apple='https://music.apple.com/us/artist/the-milbillies/1537873710',
            yt='https://youtube.com/channel/UCOxURCRCWCF2Ioc3Cg3sadg?si=w2aMAFu5hzoK_I7c'),
        BandInfo.create(
            name='John Louis',
            day='F',
            time='6:00pm - 6:30pm',
            stage='Church',
            bio="""
                John’s that guy on the bus who sits quietly, looking tired like
                the rest of us. The difference is he is sitting there composing
                a song about your life and those painful poignant moments you
                dust off on the way home between life’s chores. His songs show
                us our lives and the subtle but important things that become
                universally important hallmarks of our Midwestern journey.
                """,
            img='https://d10j3mvrs1suex.cloudfront.net/s:bzglfiles/u/397520/33e8757d56580fa654ce3ed826e9d06675ba1358/original/john-louis-011924-img-9864-copy.jpeg/!!/b%3AW1sicmVzaXplIiwxOTU3XSxbIm1heCJdLFsid2UiXV0%3D/meta%3AeyJzcmNCdWNrZXQiOiJiemdsZmlsZXMifQ%3D%3D.jpg',
            web='https://johnlouissongs.com/',
            fb='https://www.facebook.com/johnlouissongs',
            insta='https://instagram.com/johnlouissongs',
            spotify='https://open.spotify.com/artist/3wQFhoGQTCK3iCqPfYEMXa?si=wDwUMVlcQ7uFbu2y8heMWQ',
            apple='https://itunes.apple.com/artist/john-louis/1047028603',
            yt='https://www.youtube.com/channel/UCON9fn8_sPPijB8zYeRZOTA'),
        BandInfo.create(
            name='Chicago Farmer & The Fieldnotes',
            day='F',
            time='6:30pm - 7:30pm',
            stage='Main',
            bio="""
                The son of a small town farming community, Cody Diekhoff logged
                plenty of highway and stage time under the name Chicago Farmer
                before settling in the city in 2003. Profoundly inspired by
                fellow midwesterner John Prine, he’s a working-class folk
                musician to his core. His small town roots, tilled with city
                streets mentality, are turning heads North and South of I-80.
                """,
            img='https://images.squarespace-cdn.com/content/v1/5a5d77ad010027ff5b7ec0c0/1674179572636-EKH76U84FZ73T0GI9VF7/Farmer+Band+Melody+Barb+2.jpg?format=2500w',
            web='https://chicagofarmer.com/',
            fb='https://www.facebook.com/chicagofarmer/',
            insta='https://www.instagram.com/chicagofarmermusic/',
            spotify='https://open.spotify.com/artist/69MACpHHQg9ovd1retYWPq?si=Tbk22e4jShm8WL8D-5Stkw',
            apple='https://music.apple.com/us/artist/chicago-farmer/106319987',
            yt='https://www.youtube.com/channel/UCuYIdyf6wz-fBH_Y3G9hI2A'),
        BandInfo.create(
            name='Caitlen Nicol-Thomas',
            day='F',
            time='7:30pm - 8:00pm',
            stage='Church',
            bio="""
                """,
            img='https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-6/421957323_887298633395209_6722306594685577459_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=foX9hmf7OZgQ7kNvgEBR9V7&_nc_ht=scontent-msp1-1.xx&_nc_gid=AixLAh5ixoc9ggmCbE2VUtr&oh=00_AYBvLw0Na00KDmYFG11tptYrY7FwaJ6OETG4tRSV2KR6aQ&oe=67108BFB',
            fb='https://www.facebook.com/officialCNT/',
            insta='https://www.instagram.com/officialcnt/',
            apple='https://music.apple.com/us/artist/caitlin-nicol-thomas/1091723790',
            yt='https://youtube.com/channel/UCG2yUWeXJIhudh-ll0kzWrQ?si=Zz4cWXPOJqbECJFP'),
        BandInfo.create(
            name='The Fretliners',
            day='F',
            time='8:00pm - 9:00pm',
            stage='Main',
            bio="""
                It is rare for there to exist a defining moment that changes
                the trajectory of four lives at once. But, clear as a lightning
                bolt in an open field, so electric was the moment The
                Fretliners first played together around a single microphone in
                the Cloverlick banjo shop barn one fateful evening, they knew
                they would be inseparable from that moment on. The Fretliners
                are a genuine and powerful bluegrass quartet recognized for
                their songwriting and undeniable chemistry. Their newfound
                camaraderie produces an energy that is as infectious on stage
                as it is on record. So much so that in the summer of 2023, they
                won both band competitions at Telluride Bluegrass and
                Rockygrass Festivals—a feat that had only been accomplished
                once before. That September, they released their debut
                eponymous album to acclaim and adoration. With one eye on the
                rear-view, inspired by that traditional high lonesome sound,
                The Fretliners navigate a road less traveled into the peaks of
                Rocky Mountain original bluegrass.

                """,
            img='https://i.scdn.co/image/ab6761670000ecd41220f72577f42a32f81b511a',
            web='https://www.thefretliners.com/',
            fb='https://www.facebook.com/TheFretliners/',
            insta='https://www.instagram.com/thefretliners/',
            spotify='https://open.spotify.com/artist/4iMEdosOM4PPgZrreSoWJn',
            apple='https://music.apple.com/us/artist/the-fretliners/1706384107',
            yt='https://www.youtube.com/channel/UCfSoSTwH4ffhK9Dc74Iz1Gw'),
        BandInfo.create(
            name='Jaik Willis',
            day='F',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                Jaik Willis is a strumming & drumming One Man Band,  a wild
                fire-breathing freakshow; playing an 11 piece drum set with his
                feet while playing guitars / bass / & harps; while sing and
                beatboxing simultaneously, live with no looping or electronics.
                Performing 300 shows a year with appearances at Bonnaroo,
                Summer Camp Music Fest, Dunegrass, the Chicago Bluegrass &
                Blues Fests etc. Jaik Willis got a shout out in Rolling Stone
                magazine for his vocal contribution to the album “FreeStyle”
                that debuted at #1 on iTunes.
                """,
            img='https://d10j3mvrs1suex.cloudfront.net/s:bzglfiles/u/80199/9cae224b61c593c68141f59c138ab386f9f7042d/original/5274-js-jaik-willis-0268-fix.jpg/!!/b%3AW1sic2l6ZSIsInBob3RvIl1d/meta%3AeyJzcmNCdWNrZXQiOiJiemdsZmlsZXMifQ%3D%3D.jpg',
            web='https://jaikwillis.com/about',
            fb='https://www.facebook.com/JaikWillisMusic',
            insta='http://instagram.com/jaikwillis',
            spotify='https://open.spotify.com/artist/3BD4ZAvWQ5aWqNsmKPd2Un',
            apple='https://music.apple.com/us/artist/jaik-willis/268673250',
            yt='https://youtube.com/@jaikwillis?si=dpMhDsuaPGZmJHo0'),
        BandInfo.create(
            name='The Big Wu',
            day='F',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                Jam band the Big Wu formed on the campus of St. Olaf College in
                Northfield, MN in 1992 around the nucleus of singer/guitarist
                Chris Castino, guitarist Jason Fladager and drummer Terry
                VanDeWalker. Channeling a wide range of influences including
                bluegrass, rock, jazz, psychedelia and R&B, the group built a
                strong local following thanks to a rigorous live schedule,
                adding bassist Andy Miller in 1995 and keyboardist Al Oikari a
                year later. In early 1996 the Big Wu also landed their first
                weekly gig at Minneapolis' Terminal Bar, solidifying their
                fanbase and scoring a spot on the following year's H.O.R.D.E.
                Festival. Their debut album Tracking Buffalo Through the
                Bathtub appeared that autumn, and was reissued by the Big Wu's
                new label Phoenix Rising in 1999. Folktales followed a year
                later. 
                """,
            img='https://i.scdn.co/image/fd1a8e2bc5e78397e8c5d887ee621cd71dbf6c97',
            web='https://www.thebigwu.com/',
            fb='https://www.facebook.com/TheBigWu/',
            insta='https://www.instagram.com/thebigwu/',
            spotify='https://open.spotify.com/artist/2IQLjVQHKnzSQAVAkeCcQ0',
            apple='https://music.apple.com/us/artist/the-big-wu/14949567',
            yt='https://www.youtube.com/channel/UCpKmpKnY8ttL1nXE72AzUFA')
    ]
    saturday: list[BandInfo] = [
        BandInfo.create(
            name='Thomas Sticha',
            day='s',
            time='12:30pm - 1:30pm',
            stage='Main',
            bio="""
                Thomas Sticha is a Country & Folk Music Artist from Saint Paul,
                Minnesota. He’s giving new life to the heroes of Classic
                Country (to the likes of Willie Nelson, John Prine, Merle
                Haggard), while nodding to the future of Classic Country Music
                (to the likes of Tyler Childers, Zach Top, Midland).
                Thomas’ debut release, “Then It’s Gone,” made its way into the
                world on January 19, 2024.
                """,
            img='https://images.squarespace-cdn.com/content/v1/63a77a8955f5b2170c8008d6/e8b74c03-26f8-4565-a5da-65811243cbd8/IMG_1408.jpg?format=2500w',
            web='https://www.thomassticha.com/',
            fb='https://www.facebook.com/thomasstichamusic/',
            insta='https://www.instagram.com/sticha/',
            spotify='https://open.spotify.com/artist/0l16reYqmLwCXePRrQKpf4?si=qESimPEVR_OhsSW43LOe2Q',
            apple='https://music.apple.com/jm/artist/thomas-sticha/1724228680',
            yt='https://www.youtube.com/channel/UCje7Q3W3xbCrK8X0xwe5vOg'),
        BandInfo.create(
            name='The Crowd',
            day='s',
            time='1:30pm - 2:00pm',
            stage='Church',
            bio="""
                Which crowd?
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Corpse Reviver',
            day='s',
            time='2:00pm - 3:00pm',
            stage='Main',
            bio="""
                3 musicians who like to mostly play music found on Harry
                Smith’s Anthology of American Folk Music
                """,
            img='https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-6/241683366_494526511811494_1154546161558859416_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=B4mxl_4U7tEQ7kNvgHJ2-Ew&_nc_ht=scontent-msp1-1.xx&_nc_gid=AdMroc68Bkx_oPyPe_KIqwf&oh=00_AYCazSwsAJFgFbrYquLlx09XGzz0yRCluWdDBTupqugswg&oe=67109AF1',
            web='',
            fb='https://www.facebook.com/corpserevivermpls/',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Matt Fockler',
            day='s',
            time='3:00pm - 3:30pm',
            stage='Church',
            bio="""
                A gifted song-writer, two of Matt's songs were recently
                included on Jonathan Byrd and the Pick Up Cowboys' Latest album
                release. His songs have been covered by many notable
                Folk/Americana artists, including Jonathan Byrd, Charlie Roth,
                Anthony DaCosta, and the Steep Canyon Rangers.
                """,
            img='https://img1.wsimg.com/isteam/ip/b31ead5d-2c58-44fd-a0e4-4d4cec7d0513/FA275D80-4A1B-469D-8F32-F83AC01F8A47.jpeg/:/cr=t:0%25,l:0.01%25,w:99.98%25,h:100%25/rs=w:900,m',
            web='https://montrosemusicfestival.org/matt-fockler',
            fb='',
            insta='',
            spotify='https://open.spotify.com/artist/0gn4HeOEGhmcSHWxNJD0Ti',
            apple='https://music.apple.com/us/artist/matt-fockler/1606026635',
            yt='https://www.youtube.com/c/MattFockler'),
        BandInfo.create(
            name='City Mouse',
            day='s',
            time='3:30pm - 4:30pm',
            stage='Main',
            bio="""
                This band has played around Mankato since 1971. Almost every
                musician in the area has been in the group at one time or
                another. However, the lineup has been stable for the past
                thirteen years or so. The members of the band are: founder and
                leader Billy Steiner (harmonica); Dale Haefner (keyboards);
                Ron Arsenault (acoustic guitar); Mike Pengra (drums); Dave
                Pengra (base) and Tim Waters (electric and pedal steel
                guitars). All but Dale share in the vocals from time to time.
                """,
            img='https://scontent-msp1-1.xx.fbcdn.net/v/t1.6435-9/164430866_702919067102650_6789030083778296992_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=2a1932&_nc_ohc=s1CBFa7WSaIQ7kNvgH55TbT&_nc_ht=scontent-msp1-1.xx&_nc_gid=AtLL0SYmu8CdIKUjbsl3Bax&oh=00_AYBy7Ae-7VCKvlepN7XUBSvohlHfQOxVZ4hiWczCbzZbsw&oe=673254F0',
            web='',
            fb='https://www.facebook.com/p/City-Mouse-100021536894781/',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='Tommy Edwin',
            day='s',
            time='4:30pm - 5:00pm',
            stage='Church',
            bio="""
                Tommy Edwin is a singer-songwriter currently based in
                Brookings, South Dakota.
                Tommy’s repertoire includes original songs and a large
                selection of cover tunes focusing on singer-songwriters from
                the 60’s and 70’s as well as more contemporary material.
                Artists covered include James Taylor, Gordon Lightfoot, Tom
                Petty, Richard Thompson, Don McLean among others. Tommy also
                specializes in the music of  Bob Dylan, covering a wide range
                of his recordings from the the early sixties onward and has
                done entire all-Dylan shows.
                """,
            img='https://static.wixstatic.com/media/12debe_da88683f6f754cc6a56e03cada7ec9fc~mv2.jpg/v1/fill/w_1903,h_959,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/12debe_da88683f6f754cc6a56e03cada7ec9fc~mv2.jpg',
            web='https://www.tommyedwinmusic.com/',
            fb='https://www.facebook.com/people/Tommy-Edwin/100017192042873',
            insta='http://www.instagram.com/tommyedwin1212/',
            spotify='https://open.spotify.com/artist/7JC6zYIGqnRHswK8l3dk7L',
            apple='https://music.apple.com/us/artist/tommy-edwin/1632861800',
            yt='https://www.youtube.com/playlist?app=desktop&list=PL44fpVKgATb3DWPlxjhDAuplWADLXVuSR'),
        BandInfo.create(
            name='Erin McCawley\'s Harrison St. Band',
            day='s',
            time='5:00pm - 6:00pm',
            stage='Main',
            bio="""
                Singing, songwriting, sass-bringing Erin McCawley and her
                Harrison Street Band know how to entertain and energize the
                crowd with blues styles from Chicago to Louisiana and
                everything in between. Erin sings with the confidence and soul
                as if each song was the story she was born to tell and with a
                voice that seem to rise up from the soles of her feet. Her
                genuine sense of personal freedom empowers her audience and
                draws them in to each performance; then with clever lyrics,
                radiant joy, and raw emotion, she holds them there. She is
                backed by an incredible band of talented musicians: Tony Houle
                on Guitar, Robb Stearns on bass, and Bill Whelan on drums. They
                are often joined by Joey Gagliardi on harmonica, and Paul Wigen
                on keys. Together, they have released a third album of original
                music; “Live at A440.” Listen, and you may hear the blues, but
                you won’t leave with ‘em!”
                """,
            img='https://harrisonstreetband.com/wp-content/uploads/2019/11/img_7882.png?w=1200',
            web='https://harrisonstreetband.com/',
            fb='https://www.facebook.com/HarrisonStreetBand/',
            insta='https://www.instagram.com/erinmchsb/',
            spotify='https://open.spotify.com/artist/3sec2YUyotC0clXzZPZBkg',
            apple='https://music.apple.com/us/artist/harrison-street-band/1413560621',
            yt=''),
        BandInfo.create(
            name='Corpse Reviver',
            day='s',
            time='6:00pm - 6:30pm',
            stage='Church',
            bio="""
                3 musicians who like to mostly play music found on Harry
                Smith’s Anthology of American Folk Music
                """,
            img='https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-6/241683366_494526511811494_1154546161558859416_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=B4mxl_4U7tEQ7kNvgHJ2-Ew&_nc_ht=scontent-msp1-1.xx&_nc_gid=AdMroc68Bkx_oPyPe_KIqwf&oh=00_AYCazSwsAJFgFbrYquLlx09XGzz0yRCluWdDBTupqugswg&oe=67109AF1',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='The Foxgloves',
            day='s',
            time='6:30pm - 7:30pm',
            stage='Main',
            bio="""
                The Foxgloves are an Americana/newgrass band from Minneapolis.
                Their high energy performances, heartfelt storytelling,
                four-part harmonies, and musical depth have swept them onto
                big stages throughout the region, including Blue Ox Music
                Festival, First Avenue Mainroom, and Big Top Chautauqua. This
                powerful band is making moves you’ll want to witness.
                """,
            img='https://static.wixstatic.com/media/ba24ae_1a2f0baca008487798833ad8dd3b5532~mv2.png/v1/fill/w_600,h_533,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Foxgloves%20Turf.png',
            web='https://www.thefoxgloves.com/',
            fb='https://www.facebook.com/thefoxglovesband',
            insta='https://www.instagram.com/thefoxglovesband',
            spotify='https://open.spotify.com/artist/0cyz3380h6MXubEEDO6FX2',
            apple='https://music.apple.com/us/artist/the-foxgloves/1566701441',
            yt='https://www.youtube.com/channel/UCiAI1hLP-AcBZRPOHn2cGNw'),
        BandInfo.create(
            name='Mal Murphy',
            day='s',
            time='7:30pm - 8:00pm',
            stage='Church',
            bio="""
                Mal Murphy is a Mankato, MN-based singer-songwriter who
                released her first, and highly anticipated, EP in December of
                2023 entitled, “Grow Up.” Her sound is decidedly
                Americana-–acoustic accompanying rich vocals with an occasional
                harmonica. The development of Mal’s style was inspired by
                greats such as Brandi Carlile, Gregory Alan Iskob, Jade Bird,
                and Ani DiFranco. Mal’s voice is clear, bright, and powerful,
                known for snapping the casual listener in a noisy bar to
                allegiance. Her wide-ranged,versatile voice blends well in
                duets or charms as a passionate and charismatic solo artist.
                Mal’s many loyal and diverse followers gather to hear her pour
                new light into well loved classic covers, or to hear her
                traverse new landscapes with her original songs.
                """,
            img='https://malmurphymusic.com/wp-content/uploads/2023/12/IMG_6001-768x1024.jpg',
            web='https://malmurphymusic.com/',
            fb='https://www.facebook.com/MalMurphyMusic/',
            insta='https://www.instagram.com/malsarahmurphy/',
            spotify='https://open.spotify.com/artist/00f7TsKCR9BYqaQTyI5ZX8',
            apple='https://music.apple.com/us/artist/mal-murphy/1715533736',
            yt='https://www.youtube.com/channel/UCO6c5UsusP7IkgJizm_XjIQ'),
        BandInfo.create(
            name='Katy Guillen & the Drive',
            day='s',
            time='8:00pm - 9:00pm',
            stage='Main',
            bio="""
                Through the course of writing, refining and recording their
                debut full-length album, “Another One Gained,” Katy Guillen &
                The Drive delved into the catharsis of a bittersweet moment in
                time. Recorded with Kevin Ratterman (My Morning Jacket,
                Heartless Bastards) at Invisible Creature Studio in Los
                Angeles, the 10-track effort was met with high praise upon its
                2022 release. Accompanied by drummer Stephanie Williams’
                melodically exacting rhythms, Guillen’s emotive guitar playing
                aligns with her lyrics to meet at the crossroads of suffering
                and silver linings. 
                As lauded by Under The Radar Magazine, the duo evokes a “simple
                and timeless indie rock sound carried by Guillen’s chugging
                guitar and Williams’ driving drums, yet they also show off
                effortless instrumental chemistry, locking into an easygoing
                groove that gives both members a chance to shine.”
                """,
            img='https://images.squarespace-cdn.com/content/v1/642c6cddda95137b3c63cacd/f77ace80-760e-408f-b2e1-8cb121296a5c/tempImageM9n24w.jpg?format=2500w',
            web='https://katyguillenmusic.com/',
            fb='https://www.facebook.com/kgandthedrive/',
            insta='https://www.instagram.com/kgandthedrive/',
            spotify='https://open.spotify.com/artist/3Kps5aNWnobww08SmdfzRh?autoplay=true',
            apple='https://music.apple.com/us/artist/katy-guillen-the-drive/1496004202',
            yt='https://www.youtube.com/channel/UCB8Edq_HOnE1WmxospznNBw?feature=gws_kp_artist&feature=gws_kp_artist'),
        BandInfo.create(
            name='Strictly Herbal',
            day='s',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                Rooting from rural Minnesota, Strictly Herbal is a reggae group
                bringing sounds that illustrate their love and passion for
                reggae music. From the studio to the stage, Strictly Herbal
                knows how to bring around the vibes.
                """,
            img='https://i.scdn.co/image/ab6761670000ecd4c162ee4eba9ccd9a6fe35353',
            web='',
            fb='https://m.facebook.com/people/Strictly-Herbal/61554239137753/',
            insta='https://www.instagram.com/strictly.herbal/reels/',
            spotify='https://open.spotify.com/artist/4FpiKF2ADxzDFvInQnOOy1?si=GgpeacsiTMid8C5ONo8rIg',
            apple='',
            yt=''),
        BandInfo.create(
            name='Jon Sullivan Band',
            day='s',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                There are a lot of bands performing and releasing music to the
                masses - there are not many that can bring a feeling of pure
                soul.  Jon Sullivan Band is a group that can. The band is an
                ensemble including soulful guitar, sultry keyboards, driving
                bass, and a booming rhythm section.  Their music blooms from
                origins in soul, funk, rock and blues, unlocking feelings of
                nostalgia while also being something that stands in its own
                realm.  Led by the powerful, yet silky voice of Jon Sullivan,
                this band paints a picture through each song that is drenched
                in emotion, sprawling with funky melodies and leaves you with a
                feeling that you have traveled somewhere majestic.
                """,
            img='https://d10j3mvrs1suex.cloudfront.net/s:bzglfiles/u/629446/c0143cd693318d77f625cea0d8e95b6274c84fcd/original/img-0417.jpg/!!/b%3AW1sicmVzaXplIiwxODAwXSxbIm1heCJdLFsid2UiXV0%3D/meta%3AeyJzcmNCdWNrZXQiOiJiemdsZmlsZXMifQ%3D%3D.jpg',
            web='https://jonsullivanband.com/',
            fb='https://www.facebook.com/jonsullivanband/',
            insta='https://instagram.com/jonsullivanband',
            spotify='https://open.spotify.com/artist/23FBB7KARNDUnKXhzo93Pb?autoplay=true',
            apple='https://music.apple.com/us/artist/jon-sullivan-band/1597786483',
            yt='https://www.youtube.com/channel/UC6M-1lUR3oQMK6kcPjPzp7A?feature=gws_kp_artist&feature=gws_kp_artist')
    ]

    def show_toast(self):
        yield NavState.update
        return rx.toast.info(
            'Click a band to learn more about them.',
            duration=5000,
            close_button=True
        )


def on_stage_component(comp_func):
    def wrapper(band: BandInfo):
        return rx.cond(
            (band.start < NavState.now) & (band.end > NavState.now),
            comp_func(band),
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
                rx.dialog.title(band.name),
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
