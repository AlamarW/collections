module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick)


-- MODEL


type alias Model =
    {}


init : () -> ( Model, Cmd Msg )
init _ =
    ( {}
    , Cmd.none
    )


-- UPDATE


type Msg
    = LoginClicked


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        LoginClicked ->
            -- Login doesn't work yet
            ( model, Cmd.none )


-- VIEW


view : Model -> Html Msg
view model =
    div [ class "container" ]
        [ node "header" []
            [ div [ class "header-content" ]
                [ div [ class "logo" ] [ text "Collections Manager" ]
                , button [ class "login-button", onClick LoginClicked ]
                    [ text "Login" ]
                ]
            ]
        , div [ class "homepage" ]
            [ div [ class "hero" ]
                [ h1 [] [ text "Collections Manager" ]
                , p [ class "tagline" ] [ text "Your personal cataloging system for the things you collect" ]
                , p [ class "description" ]
                    [ text "Whether it's vinyl records, trading cards, books, or vintage toys—keeping track of your collections shouldn't be complicated. Define custom schemas for each collection and maintain detailed records of every item. No more spreadsheets, no more guesswork. Just organized, accessible data about the things you love to collect." ]
                , p [ class "note" ] [ text "(Login functionality not yet implemented)" ]
                ]
            ]
        ]


-- MAIN


main : Program () Model Msg
main =
    Browser.element
        { init = init
        , view = view
        , update = update
        , subscriptions = \_ -> Sub.none
        }
