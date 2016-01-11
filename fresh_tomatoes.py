import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Mayhem!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" type="text/css" href="font-awesome.min.css">
    <script src="http://code.jquery.com/jquery-1.12.0.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }

        .movie-tile {
            position:relative;
            box-shadow:inset 1px 1px 40px 0 rgba(0,0,0,.45);
        }
        .movie-tile:hover {
            background-color: black;
            cursor: pointer;
        }
        #overlay{
            position:relative;
            height:400px;
            width:280px;
            background:rgba(0,0,0,.75);
            text-align:center;
            opacity:0;
            -webkit-transition: opacity .25s ease;
            -moz-transition: opacity .25s ease;
            margin-left: -15px;
        }
        .movie-tile:hover #overlay {
            opacity:1;
        }
        #title {
            font-family:Helvetica;
            font-weight:900;
            color:rgba(255,255,255,.85);
            font-size:28px;
            height: 25%;
        }
        #synopsis {
            color:rgba(255,255,255,.85);
            height: 150px;
            text-align: center;
            overflow:auto;
            padding-left: 25px;
            padding-right:25px;
        }
        .bold {font-weight:900;}

        #buttons{
            padding-top:20px;
            font-family:Helvetica;
            color:rgba(255,255,255,.85);
            font-size:14px;
            height:25%;
        }

        button {
            border-radius:24px;
            }
    
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.tryme', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Mayhem Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" style="background-image:url({poster_image_url}); background-size:cover; height:400px; width:280px;" >
    <!--MOVIE INFORMATION PANEL THAT DISPLAYS ON HOVER-->
    <div id="overlay">
       <div id="title">{movie_title} ({year})</div>
       <!--SCROLLING MOVIE INFORMATION SECTION-->
       <div id="synopsis">
            <div><span class="bold">Rated:</span> </br>{rating}</div></br>
            <div><span class="bold">Starring:</span>  </br>{stars}</div></br>
            <div><span class="bold">Synopsis:</span>  </br>{synopsis}</div>
       </div>

       <!--BUTTONS TO VIEW TRAILER AND DOWNLOAD WALLPAPER-->
       <form>
       <div id="buttons">
            <a href="#"  class="tryme btn btn-warning btn-sm" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Watch Trailer</a></br>
            <a href="{wallpaper}" download="{movie_title}-wallpaper" class="btn btn-warning btn-sm">Download Wallpaper</a>
       </div>
       </form>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            synopsis=movie.storyline,
            trailer_youtube_id=trailer_youtube_id,
            wallpaper=movie.wallpaper,
            stars=movie.starring,
            rating=movie.rating,
            year=movie.year
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
