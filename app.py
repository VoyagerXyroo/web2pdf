from flask import Flask, request, send_file, render_template_string
import pdfcrowd
import io

app = Flask(__name__)

# HTML template untuk halaman utama
form_html = '''
<!DOCTYPE html>
<html
  lang="en"
>
  <head>
    <meta charset="utf-8" />
    <title>Convert</title>
    <meta
      content="We Convert Your Website to PDF"
      name="description"
    />
    <meta content="Contact" property="og:title" />
    <meta
      content="We Convert Your Website to PDF"
      property="og:description"
    />
    <meta
      content="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/arya.png"
      property="og:image"
    />
    <meta content="Contact" property="twitter:title" />
    <meta
      content="We Convert Your Website to PDF"
      property="twitter:description"
    />
    <meta
      content="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/arya.png"
      property="twitter:image"
    />
    <meta property="og:type" content="website" />
    <meta content="summary_large_image" name="twitter:card" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <link
      href="https://assets-global.website-files.com/6618e637b1708fa9ebdf54ae/css/lot-experience.674083b72.css"
      rel="stylesheet"
      type="text/css"
    />
    <script type="text/javascript">
      !(function (o, c) {
        var n = c.documentElement,
          t = " w-mod-";
        (n.className += t + "js"),
          ("ontouchstart" in o ||
            (o.DocumentTouch && c instanceof DocumentTouch)) &&
            (n.className += t + "touch");
      })(window, document);
    </script>
    <link
      href="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/logo.png"
      rel="shortcut icon"
      type="image/x-icon"
    />
    <link
      href="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/logo.png"
      rel="apple-touch-icon"
    />

    <script>
      var imageUrl =
        "https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/arya.png";
      var imageWidth = 1920; // Replace with your image width
      var imageHeight = 1080; // Replace with your image height

      // Create og:image meta tag
      var ogImageTag = document.createElement("meta");
      ogImageTag.setAttribute("property", "og:image");
      ogImageTag.setAttribute("content", imageUrl);
      document.head.appendChild(ogImageTag);

      // Create og:image:width meta tag
      var ogImageWidthTag = document.createElement("meta");
      ogImageWidthTag.setAttribute("property", "og:image:width");
      ogImageWidthTag.setAttribute("content", imageWidth);
      document.head.appendChild(ogImageWidthTag);

      // Create og:image:height meta tag
      var ogImageHeightTag = document.createElement("meta");
      ogImageHeightTag.setAttribute("property", "og:image:height");
      ogImageHeightTag.setAttribute("content", imageHeight);
      document.head.appendChild(ogImageHeightTag);
    </script>

    <style>
      body::before {
        content: "";
        width: 100%;
        height: 0%;
        background: linear-gradient(
          66deg,
          rgba(169, 45, 76, 1) 24%,
          rgba(95, 42, 87, 1) 100%
        );
        position: fixed;
        bottom: 0;
        left: 0;
        transition: all 0.8s cubic-bezier(0.89, 0.14, 0, 0.99);
        z-index: 99999999;
      }
      body::after {
        content: "";
        width: 100%;
        height: 100%;
        background: linear-gradient(
          66deg,
          rgba(169, 45, 76, 1) 24%,
          rgba(95, 42, 87, 1) 100%
        );
        position: fixed;
        top: 0;
        left: 0;
        transition: all 0.8s cubic-bezier(0.89, 0.14, 0, 0.99);
        z-index: 99999999;
      }
      .body-loaded {
        opacity: 1;
      }
      .body-loaded::after {
        height: 0% !important;
      }
      .body-loader::before {
        height: 100% !important;
      }
      .red-glow {
        animation: shrinkAndGrow 6s ease-in-out infinite alternate;
      }
    </style>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
  </head>
  <body class="inner-page-white">
    <div class="components">
      <div class="css">
        <div class="css-root w-embed">
          <style>
            @import url("https://fonts.cdnfonts.com/css/dm-sans");

            :root {
              --black: #050512;
              --beige: #fffbfb;
              --grey: #808080;
              --red: #a2254b;
              --soft-red: #d4bdc4;
              --red-brown: #938388;
              --mid-brown: #4c3e43;
            }
            html.lenis {
              height: auto;
            }
            .lenis.lenis-smooth {
              scroll-behavior: auto !important;
            }
            .lenis.lenis-smooth[data-lenis-prevent] {
              overscroll-behavior: contain;
            }
            .lenis.lenis-stopped {
              overflow: hidden;
            }
            .lenis.lenis-scrolling iframe {
              pointer-events: none;
            }
            html,
            body {
              overflow-x: hidden;
            }
            body {
              padding: 0;
              margin: 0;
              background: var(--black);
              color: var(--beige);
              font-size: 1vw;
              line-height: 1.3;
              overflow: -moz-scrollbars-none;
              -ms-overflow-style: none;
              font-family: "DM Sans", sans-serif;
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
              text-rendering: optimizeLegibility;
              letter-spacing: -0.01vw;
              scrollbar-width: none;
              cursor: default;
            }
            img {
              user-select: none;
              -moz-user-select: none;
              -webkit-user-drag: none;
              -webkit-user-select: none;
              -ms-user-select: none;
              max-width: 100%;
              object-fit: cover;
            }
            h1,
            h2,
            h3,
            .menu,
            .numbers-highlights h4,
            .menu-button,
            .label-text,
            .submit {
              font-family: "PPMonumentExtended-Medium";
              text-transform: uppercase;
            }
            a {
              color: unset;
              text-decoration: unset;
            }
            * {
              -webkit-tap-highlight-color: transparent;
              -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            }
            ::selection {
              background: #ae2c4b;
              color: #ffffff;
            }
            ::-webkit-scrollbar {
              display: none;
            }
            canvas {
              background-color: transparent;
              pointer-events: none !important;
            }
            h1,
            h2,
            h3,
            h4,
            h5,
            h6,
            p {
              padding: 0;
              margin: 0;
              font-weight: unset;
            }
            h1 {
              font-size: 7.5em;
              line-height: 0.83;
              font-weight: 400;
              letter-spacing: -0.5vw;
            }
            h2 {
              font-size: 3.5em;
              line-height: 1.1;
              font-weight: 400;
              letter-spacing: -0.2vw;
            }
            h3 {
              font-size: 2.4em;
              line-height: 1;
              font-weight: 400;
              letter-spacing: -0.15vw;
            }
            h4 {
              font-size: 1.7em;
              line-height: 1.35;
              font-weight: 400;
              letter-spacing: -0.04vw;
            }
            h5 {
              font-size: 1em;
              line-height: 1.5;
              color: var(--grey);
            }
            h6 {
              text-transform: uppercase;
              line-height: 1.5;
              color: var(--white);
              font-size: 0.8em;
              letter-spacing: 0.1vw;
            }
            p {
              margin-top: 1vw;
              font-size: 1em;
              line-height: 1.35;
              color: var(--grey);
            }
            .page {
              padding: 5.5vw;
            }
            .nav {
              display: grid;
              grid-template-columns: repeat(12, 1fr);
              padding: 6vw;
              padding-right: 5.5vw;
              padding-left: 5.5vw;
              top: 5.5vw;
              min-width: 100vw;
              margin: auto;
              justify-content: end;
              align-items: center;
              margin: auto !important;
              z-index: 3;
              left: 50%;
              transform: translate(-50%, -50%);
              padding-top: 0;
              padding-bottom: 0;
              height: 6.5vw;
              padding-top: 0vw;
              position: fixed !important;
              -webkit-user-select: none; /* Safari */
              -ms-user-select: none; /* IE 10 and IE 11 */
              user-select: none; /* Standard syntax */
              transition: top 0.3s ease, background 0.3s ease, padding 0.3s ease !important; /* Added transition for smooth movement */
            }
            .nav.fixed {
              position: fixed !important;
              padding-right: 5.5vw;
              padding-left: 5.5vw;
              min-width: 100vw;
              background: rgb(5, 5, 18, 1);
              height: 6.5vw;
              padding-top: 1vw;
              top: 2.4vw;
              -webkit-box-shadow: 0px 0px 50px 0px rgba(0, 0, 0, 0.04);
              -moz-box-shadow: 0px 0px 50px 0px rgba(0, 0, 0, 0.04);
              box-shadow: 0px 0px 50px 0px rgba(0, 0, 0, 0.04);
              transition: background 0.3s ease, padding 0.3s ease, top 0.3s ease !important; /* Added transition for smooth movement */
            }
            .nav.hide {
              top: -3.5vw !important;
              transition: top 0.3s cubic-bezier(0.27, 0, 0, 0.99) !important;
            }
            .logo {
              grid-column: 1/1;
            }
            .logo img {
              min-width: 6vw;
              max-width: 6vw;
            }
            .burger {
              display: none;
            }
            .menu-overlay {
              display: none;
            }
            .menu {
              grid-column: 8/13;
              display: flex;
              justify-content: space-between;
              align-items: center;
              position: relative;
              font-size: 0.7em;
            }
            #menu-link {
              margin-top: 0.35vw;
            }
            .menu .nav-cta {
              padding: 1vw 1.5vw;
              border-radius: 0.3vw;
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
              background-size: 100% 100%;
              transition: background 0.5s ease;
            }
            .menu .nav-cta:hover {
              background-size: 200% 200%;
            }
            .split-parent,
            .split-child {
              overflow-y: hidden !important;
              white-space: nowrap;
            }
            h1 .split-parent {
              overflow-x: visible !important;
              padding-bottom: 0vw;
              margin-bottom: -1.2vw;
            }
            h1 .split-child {
              padding-bottom: 1.7vw;
              padding-right: 0vw;
              overflow-x: visible !important;
            }
            #cursor {
              position: fixed;
              z-index: 9999999999 !important;
              left: 0;
              top: 0;
              border-radius: 100%;
              pointer-events: none;
              will-change: transform;
              mix-blend-mode: difference;
            }
            .grid-line {
              position: relative;
            }
            .section {
              position: relative;
              margin-bottom: 13vw;
            }
            .contact .section {
              margin-bottom: 0vw;
            }
            .eyebrow {
              display: flex;
              border-radius: 50vw;
              border: 0.8px solid var(--white);
              text-transform: uppercase;
              position: absolute;
              justify-content: center;
              padding: 0.3vw 0.8vw;
              grid-gap: 0.7vw;
              align-items: center;
              top: 0;
              left: 0;
            }
            .eyebrow h5 {
              color: var(--white) !important;
              letter-spacing: 0.1vw;
              font-size: 0.7em;
            }
            .red-dot {
              background-color: var(--red) !important;
              border-radius: 50vw;
              width: 0.5vw;
              height: 0.5vw;
              -webkit-user-select: none;
              -ms-user-select: none;
              user-select: none;
            }
            @media (hover: hover) and (pointer: fine) {
              .cursor__circle {
                width: 4vw;
                height: 4vw;
                border-radius: 100%;
                border: solid 1.5px var(--beige);
                transition: all 0.4s cubic-bezier(0.52, 0.02, 0, 0.99);
              }
              #cursor.overlay .cursor__circle {
                width: 0.5vw;
                height: 0.5vw;
                background-color: var(--beige);
                border-color: transparent;
              }
              #cursor.explore-overlay .cursor__circle {
                background: var(--beige);
                border-color: transparent;
                width: 8vw;
                height: 8vw;
                transition: all 0.4s cubic-bezier(0.52, 0.02, 0, 0.99);
              }
              #cursor.explore-overlay .cursor__circle::after {
                content: "Explore";
                display: block;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: black;
                font-size: 0.8em;
                line-height: 1;
                transition: all 0.4s cubic-bezier(0.52, 0.02, 0, 0.99);
              }
              .explore-overlay {
                backdrop-filter: blur(10px);
              }
            }
            @media only screen and (min-width: 600px) {
              .lottie-mobile {
                display: none;
              }
            }

            @media only screen and (max-width: 600px) {
              [class^="g-c-"] {
                display: flex;
                flex-direction: column;
              }
              .cursor__circle {
                display: none;
              }
              .number-span {
                font-size: 4vw !important;
              }
              h1 {
                font-size: 14em;
                line-height: 0.83;
                font-weight: 400;
                letter-spacing: -0.5vw;
              }
              h2 {
                font-size: 7em;
                line-height: 1.1;
                font-weight: 400;
                letter-spacing: -0.2vw;
              }
              h3 {
                font-size: 5.9em;
                line-height: 1;
                font-weight: 400;
                letter-spacing: -0.15vw;
              }
              h4 {
                font-size: 5em;
                line-height: 1.35;
                font-weight: 400;
                letter-spacing: -0.04vw;
              }
              h5 {
                font-size: 1em;
                line-height: 1.5;
                color: var(--grey);
              }
              h6 {
                text-transform: uppercase;
                line-height: 1.5;
                color: var(--white);
                font-size: 2.5em;
                letter-spacing: 0.1vw;
              }
              p {
                margin-top: 1vw;
                font-size: 3.2em;
                line-height: 1.35;
                color: var(--grey);
              }
              .grid {
                display: flex !important;
              }
              .block-space {
                margin-top: 10vw;
                margin-bottom: 10vw;
              }
              .eyebrow {
                padding: 0.6vw 2vw;
                grid-gap: 0.7vw;
                align-items: center;
                top: 0;
                left: 0;
              }
              .eyebrow h5 {
                font-size: 2.4em;
              }
              .red-dot {
                width: 1.4vw;
                height: 1.4vw;
                margin-right: 1vw;
              }
              .section {
                margin-top: 25vw;
                margin-bottom: 25vw;
              }
              .no-margin {
                margin: 0 !important;
                padding: 0 !important;
              }
              .nav {
                display: grid;
                grid-template-columns: repeat(12, 1fr);
                margin: 5.5vw;
                top: 5vw;
                width: unset;
                margin: auto;
                justify-content: end;
                align-items: center;
                margin: auto !important;
                background: transparent;
                z-index: 3;
                left: unset;
                transform: unset;
                position: relative !important;
                transition: background 0.3s ease, padding 0.3s ease !important; /* Added transition for smooth movement */
              }
              .menu {
                background: white;
                position: fixed;
                display: flex;
                flex-direction: column !important;
                justify-content: start;
                align-items: start;
                grid-gap: 5vw;
                padding: 8vw;
                padding-right: 0;
                padding-top: 10vw;
                border-radius: 5vw 0vw 0vw 0vw;
                bottom: 0;
                right: 0;
                color: black;
              }
              .logo img {
                min-width: 18vw;
                max-width: 18vw;
              }
              .menu .nav-cta {
                padding: 3vw 5vw;
                border-radius: 1vw;
                color: var(--beige) !important;
                font-size: 2.9vw !important;
              }
              .menu {
                grid-column: 4/12;
                font-size: 6em;
                flex-direction: row;
                transform: translate(100%, 100%);
              }
              .menu-overlay {
                background: rgba(5, 5, 18, 0.3);
                height: 100vh;
                width: 100%;
                position: fixed;
                top: 0;
                left: 0;
                z-index: 0;
                opacity: 0;
                display: none;
              }
              .menu-trigger {
                width: 30vw;
                height: 18vw;
                position: fixed;
                top: 0;
                right: 0;
                z-index: 9999999;
              }
              .burger {
                display: flex;
                position: fixed;

                right: 5vw;
                mix-blend-mode: difference;
              }
              .menu-button {
                margin-top: 2.7vw;
                font-size: 3.6vw;
                letter-spacing: 0.5vw;
                text-align: right;
                height: 5vw;
                flex-direction: column;
                overflow: hidden;
              }
              .menu .link {
                counter-increment: linkCounter;
                position: relative;
                left: -10vw;
              }

              .menu .link:before {
                content: counter(linkCounter, decimal-leading-zero);
                margin-left: 5vw;
                position: relative;
                font-size: 5px;
                top: -7vw;
                left: 5vw;
                color: var(--red);
                border: 0.5px solid var(--red);
                border-radius: 50vw;
                padding: 0vw 0.8vw;
              }
            }
          </style>
        </div>
        <div class="main-css w-embed">
          <style>
            .homepage .page {
              padding-top: 15vw;
            }
            .hero-section {
              display: flex;
              flex-direction: column;
              justify-content: space-between;
            }
            .hero {
              display: grid;
              grid-template-columns: repeat(12, 1fr);
              height: 100vh;
            }
            video,
            .video {
              display: none;
            }
            .hero-visual {
              width: 100vw;
              height: 100%;
              position: absolute;
              top: 0;
              z-index: 2;
              pointer-events: none;
            }
            .hero-bottom-text {
              display: flex;
              justify-content: space-between;
              align-items: end;
              position: absolute;
              left: 5.5vw;
              right: 5.5vw;
              bottom: 5.5vw;
              font-size: 0.8em;
            }
            .hero-heading h1 {
              margin-left: -0.4vw;
            }
            .hero-heading h4 {
              margin-bottom: 1.5vw;
              font-weight: 500;
              letter-spacing: -0.09vw;
            }
            .hero-down-arrow {
              min-width: 5vw;
              max-width: 5vw;
            }
            .red-glow {
              background: #3a0f24;
              border-radius: 20vw;
              width: 40vw;
              height: 40vw;
              filter: blur(100px);
              z-index: -1;
              pointer-events: none;
              position: absolute;
            }
            @keyframes shrinkAndGrow {
              0% {
                transform: scale(0.8);
              }
              50% {
                transform: scale(1.7);
              }
              100% {
                transform: scale(0.8);
              }
            }
            .glow-left {
              bottom: -20vw;
              left: -25vw;
            }
            .glow-right {
              bottom: -20vw;
              right: -25vw;
            }
            .home-intro-text {
              color: var(--soft-red);
            }
            .home-image-1 {
              min-width: 30vw;
              max-width: 30vw;
            }
            .home-image-2 {
              min-width: 15vw;
              max-width: 15vw;
            }
            .big-marquee {
              margin-bottom: 10vw;
              width: 120%;
              left: -10vw;
              white-space: nowrap;
              overflow: hidden;
              position: relative;
              font-family: "PPMonumentExtended-Medium";
              text-transform: uppercase;
            }
            .big-marquee div {
              display: inline-block;
              animation: marquee 20s linear infinite;
              font-size: 18vw;
              letter-spacing: -0.9vw;
              padding: 5vw 5vw;
            }
            @keyframes marquee {
              0% {
                transform: translateX(0%);
              }
              100% {
                transform: translateX(-100%);
              }
            }
            .splide {
              margin-bottom: 15vw !important;
            }
            .splide__list {
              display: flex;
              grid-gap: 5vw;
            }
            .splide__slide {
              min-width: 30vw;
              max-width: 30vw;
              min-height: 29vw;
              max-height: 29vw;
              padding: 3vw;
              display: flex;
              flex-direction: column;
              grid-gap: 1vw;
              position: relative;
            }
            .splide__slide h3 {
              flex-wrap: wrap;
              max-width: 25vw;
            }
            .slide-icon {
              margin-top: 5.3vw;
              min-width: 5vw;
              max-width: 5vw;
            }
            .explore-btn {
              font-family: "PPMonumentExtended-Medium";
              text-transform: uppercase;
              padding: 0.6vw 1.5vw;
              border-radius: 2vw;
              font-size: 0.9em;
              background: rgb(169, 45, 76);
              margin: auto;
              position: absolute;
              bottom: 1.8vw;
              right: 2vw;
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
            }
            .why-bullets {
              display: flex;
              flex-wrap: wrap;
              grid-gap: 5vw;
            }
            .why-bullet {
              width: 43%;
              padding-left: 2vw;
              border-left: 1px solid var(--red);
            }
            .why-bullet p {
              color: var(--red-brown);
            }
            .why-us-split-container {
              display: flex;
              grid-gap: 4.5vw;
            }
            .numbers-split .image {
              min-width: 24vw;
              max-width: 24vw;
            }
            .numbers-container {
              display: flex;
              flex-direction: column;
              grid-gap: 2vw;
              justify-content: space-between;
            }
            .numbers-highlights {
              display: flex;
              flex-direction: column;
              grid-gap: 1vw;
            }
            .numbers-highlights h3 {
              color: var(--red);
              font-size: 5vw;
              letter-spacing: -2w !important;
            }
            .numbers-highlights h4 {
              font-size: 1.3vw;
            }
            .cta-circle {
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
              width: 9vw;
              height: 9vw;
              border-radius: 100vw;
              display: flex;
              justify-content: center;
              align-items: center;
              position: absolute;
            }
            .cta-circle img {
              min-width: 2.5vw;
              max-width: 2.5vw;
              position: absolute;
            }
            .cta-text-block {
              height: 3.8vw;
              overflow: hidden;
              margin-left: 12vw;
            }
            .cta-container {
              grid-gap: flex;
              justify-content: start;
              align-items: center;
              grid-gap: 2.5vw;
              overflow: hidden;
            }
            .footer {
              margin-top: 15vw;
            }
            .footer-logo {
              display: flex;
              justify-content: start;
              align-items: start;
            }
            .footer-logo img {
              min-width: 18vw;
              max-width: 18vw;
              align-self: end;
            }
            .fc h3 {
              font-size: 1.3vw;
              letter-spacing: -0.02vw;
              margin-bottom: 2vw;
            }
            .fc p {
              color: var(--red-brown);
              line-height: 1.6;
            }
            .footer-menu {
              display: inline-flex;
              flex-direction: column;
              grid-gap: 0.8vw;
              justify-content: start;
              align-items: start;
            }
            .footer-menu a {
              color: var(--red-brown);
              text-align: left;
            }
            .link {
              z-index: 10;
              text-decoration: none;
              padding-bottom: 0.2vw;
            }
            .link:after {
              display: block;
              content: "";
              border-bottom: solid 1px #fff;
              transform: scaleX(0);
              transition: transform 300ms ease-in-out;
              transform-origin: 100% 0%;
              padding-bottom: 0.2vw;
              margin: auto;
              text-align: left;
            }
            .link:hover:after {
              transform: scaleX(1);
              transform-origin: 0 50%;
            }
            @media only screen and (max-width: 600px) {
              .link:after {
                display: none !important;
              }
              video,
              .video {
                display: flex;
                min-width: 100vw !important;
                max-width: 100vw !important;
                height: 100vw !important;
                position: absolute;
                top: 15vh;
                left: 0vw;
                border-radius: 100vw;
                overflow: hidden !important;
              }
              .hero-visual {
                display: none;
              }
              .red-glow {
                background: #3a0f24;
                border-radius: 20vw;
                width: 40vw;
                height: 40vw;
                filter: blur(30px);
                z-index: -1;
                pointer-events: none;
                position: absolute;
              }
              .home-image-1 {
                min-width: 50vw;
                max-width: 50vw;
              }
              .home-image-2 {
                min-width: 30vw;
                max-width: 30vw;
                position: relative;
                top: 10vw;
                left: 6.5vw;
              }
              .big-marquee {
                margin-top: 25vw;
                margin-bottom: 25vw;
              }
              .splide {
                top: 15vw !important;
                margin-bottom: 15vw !important;
              }
              .splide__slide {
                min-width: 70vw;
                max-width: 70vw;
                min-height: 69vw;
                max-height: 69vw;
                padding: 6vw;
              }
              .splide__slide h3 {
                max-width: 100% !important;
              }
              .slide-icon {
                margin-top: 9vw;
                min-width: 15vw;
                max-width: 15vw;
              }
              .explore-btn {
                padding: 1.5vw 3vw;
                border-radius: 2vw;
                font-size: 2em;
                position: absolute;
                bottom: 5vw;
                right: 5vw;
              }
              .why-bullets {
                grid-gap: 13vw;
                padding-left: 22vw;
              }
              .why-bullet {
                width: 100%;
                padding-left: 5vw;
              }
              .why-bullet p {
                margin-top: 5vw;
              }
              .why-us {
                padding-top: 1vw !important;
              }
              .why-us-split-container {
                display: flex;
                flex-direction: column-reverse;
                grid-gap: 15vw;
              }
              .numbers-split .image {
                min-width: 60vw;
                max-width: 60vw;
                position: relative;
                left: 20vw;
              }
              .numbers-container {
                display: flex;
                flex-direction: column;
                grid-gap: 8vw;
                justify-content: space-between;
              }
              .numbers-highlights {
                display: flex;
                flex-direction: column;
                grid-gap: 2vw;
                position: relative;
                left: 20vw;
              }
              .numbers-highlights h3 {
                font-size: 18vw;
                letter-spacing: -1.7vw;
              }
              .numbers-highlights h4 {
                font-size: 4vw;
              }
              .cta-text-block {
                height: 6.4vw;
                overflow: hidden;
                margin-left: 26vw;
              }
              .cta-circle {
                width: 20vw;
                height: 20vw;
              }
              .cta-circle img {
                min-width: 7vw;
                max-width: 7vw;
              }
              .cta-container {
                margin-top: 15vw;
                grid-gap: 5.5vw;
              }
              .footer .section {
                display: flex !important;
                flex-direction: column-reverse !important;
              }
              .footer-column {
                display: flex;
                flex-direction: column;
                grid-gap: 10vw;
              }
              .fc h3 {
                font-size: 4.5vw;
                letter-spacing: -0.02vw;
                margin-bottom: 6vw;
              }
              .fc p,
              .fc a {
                color: var(--red-brown);
                font-size: 3.5vw;
              }
              .fc a {
                line-height: 2;
              }
              .footer-logo {
                margin-top: 8vw;
              }
              .footer-logo img {
                min-width: 100%;
              }
            }
          </style>
        </div>
        <div class="about-css w-embed">
          <style>
            .inner-page-white {
              background: var(--beige);
              color: var(--black);
            }
            .inner-page-white .link:after {
              border-color: var(--black) !important;
            }
            .inner-page-white h4,
            .inner-page-white p,
            .inner-page-white .home-intro-text {
              color: var(--mid-brown) !important;
            }
            .inner-page-white .red-glow {
              display: none;
            }
            .inner-page-white .nav-cta {
              color: var(--beige);
            }
            .inner-page-white .eyebrow h5 {
              color: var(--black) !important;
            }
            .inner-page-white .eyebrow {
              border-color: var(--black) !important;
            }
            .inner-page .inner-hero {
              margin-top: 6vw;
            }
            .inner-page .inner-page-intro {
              max-width: 55vw;
              margin: auto;
            }
            .inner-page-white .nav.fixed {
              background: rgb(255, 251, 251, 1);
            }
            .inner-page .inner-big-heading {
              margin-bottom: 5vw;
            }
            .inner-page .inner-big-heading h1 {
              font-size: 8vw;
              display: flex;
              max-width: 0vw;
              margin: auto;
              justify-content: center;
              align-items: center;
              text-align: center;
            }
            .inner-page .inner-page-intro {
              text-align: center;
              color: var(--mid-brown);
            }
            .inner-page-white .about-image-1 {
              min-width: 28vw;
              max-width: 28vw;
            }
            .inner-page-white .about-image-2 {
              min-width: 30vw;
              max-width: 30vw;
              position: relative;
              top: 21.5vw;
            }
            .inner-page-white .inner-page .big-marquee {
              position: relative;
              top: 0vw;
              z-index: -1;
              margin-top: -30vw;
              color: #eee7e7;
            }
            .inner-page-white .about-why-box {
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
              background-size: 100% 100%;
              border-radius: 1vw;
              height: 30vw;
              display: flex;
              justify-content: center;
              align-items: center;
            }
            .inner-page-white .about-why-box img {
              min-width: 8vw;
              max-width: 8vw;
            }
            .inner-page-white .about-partner-box {
              margin-top: 2vw;
              background: #f6f1f1;
              padding: 3vw;
              border-radius: 1vw;
            }
            .inner-page-white .delphi-image {
              min-width: 12vw;
              max-width: 12vw;
              margin-bottom: 2vw;
            }
            .inner-page-white .partner-split-box {
              display: flex;
              grid-gap: 6vw;
              justify-content: center;
              align-items: start;
            }
            .inner-page-white .footer .link {
              color: var(--mid-brown) !important;
            }
            .inner-page-white .why-text-block {
              display: flex;
              flex-direction: column;
              grid-gap: 2vw !important;
            }
            .inner-page-white .why-us {
              margin-top: 20vw;
            }
            .inner-page-white .why-us .section {
              margin-top: -5vw !important;
            }
            @media only screen and (max-width: 600px) {
              .inner-page .inner-hero {
                margin-top: 17vw;
              }
              .inner-page .inner-big-heading h1 {
                font-size: 11vw;
              }
              .inner-page .inner-page-intro {
                max-width: 100%;
                margin: auto;
              }
              .inner-page-white .why-us .section {
                display: flex;
                flex-direction: column;
                margin-bottom: -5vw;
              }
              .inner-page-white .partners .section {
                display: flex;
                flex-direction: column-reverse;
                padding-top: 15vw !important;
              }
              .inner-page-white .why-text-block {
                align-self: start !important;
              }
              .inner-page-white .why-text-block p {
                margin-top: -4vw !important;
                margin-bottom: 4vw !important;
              }
              .inner-page-white .about-why-box img {
                min-width: 22vw;
                max-width: 22vw;
              }
              .inner-page-white .about-why-box {
                height: 70vw;
              }
              .inner-page-white .partner-split-box {
                flex-direction: column;
                justify-content: start;
                align-items: start;
                grid-gap: 5vw;
                padding: 5vw;
              }
              .inner-page-white .partner-split-box img {
                min-width: 30vw;
                max-width: 30vw;
              }
              .inner-page-white .why-text-block {
                margin-top: 10vw !important;
              }
              .inner-page-white .partner-split-box p {
                margin-top: 6vw;
              }
              .inner-page-white .about-image-1 {
                min-width: 42vw;
                max-width: 42vw;
              }
              .inner-page-white .about-image-2 {
                min-width: 40vw;
                max-width: 40vw;
                position: relative;
                top: 21.5vw;
                left: 5vw;
              }
            }
          </style>
        </div>
        <div class="services-css w-embed">
          <style>
            .services-page .inner-page-intro img {
              min-width: 48vw;
              max-width: 48vw;
            }
            .services-page h4,
            .services-page p,
            .services-page .home-intro-text {
              color: var(--soft-red);
            }
            .our-services .section {
              margin-top: 10vw !important;
              margin-bottom: 10vw !important;
            }
            .service-name-box {
              display: flex;
              flex-direction: column;
              grid-gap: 2vw;
              justify-content: start;
              align-items: start;
            }
            .service-name-box p {
              margin-top: 0 !important;
            }
            .service-name-box h5 {
              display: inline-block;
              font-size: 1.5vw;
              justify-content: start;
              align-items: start;
              color: var(--red);
              border: 0.5px solid var(--beige);
              border-radius: 50vw;
              padding: 0vw 0.8vw;
              line-height: 1.3;
              font-family: "PPMonumentExtended-Medium";
            }
            .service-box-image img {
              min-width: 25vw;
              max-width: 25vw;
            }
            .service-all-bullets {
              margin-top: 3vw;
              display: flex;
              flex-direction: column;

              overflow: hidden;
            }
            .service-bullets {
              display: flex;
              flex-wrap: wrap;
              grid-gap: 4vw;
            }
            .service-bullets h3 {
              font-size: 1.6vw;
              line-height: 1.1;
            }
            .service-bullet {
              flex: 1;
              min-width: 24%;
              padding-left: 2vw;
              border-left: 1px solid var(--red);
            }
            .service-bullet p {
              color: var(--red-brown);
            }
            .seemore {
              display: flex;
              justify-content: center;
              align-items: center;
              grid-gap: 1.2vw;
              border: 1px solid var(--beige);
              border-radius: 2vw;
              padding: 1.3vw 1.5vw;
            }
            .seemore h3 {
              font-size: 0.7vw;
              letter-spacing: 0.2vw;
              margin-left: 1vw;
              transition: margin 0.5s cubic-bezier(0.33, 0, 0, 0.99);
            }
            .seemore:hover h3 {
              margin-left: 3vw;
              transition: margin 0.5s cubic-bezier(0.33, 0, 0, 0.99);
            }
            .go-to-page {
              border: 1px solid black;
              color: var(--black);
              padding: 1.3vw 2vw;
              border-radius: 2vw;
              border: 1px solid var(--beige);
              background: linear-gradient(to right, black 50%, white 50%);
              background-size: 200% 100%;
              background-position: right bottom;
              transition: all 0.5s cubic-bezier(0.58, 0.08, 0, 0.99);
            }

            .go-to-page:hover {
              color: var(--beige);
              background-position: left bottom;
            }
            .go-to-page h3 {
              font-size: 0.7vw;
              letter-spacing: 0.2vw;
            }
            .plus-minus-icon {
              display: flex;
              flex-direction: column;
            }
            .plus-minus-icon img {
              position: absolute;
              min-width: 1.1vw;
              max-width: 1.1vw;
              margin-top: -0.1vw;
            }
            .plus-minus-icon .line-2 {
              transform: rotate(90deg);
            }
            .section-indicator {
              position: relative;
              top: -15vw;
              min-height: 2vw;
              min-width: 2vw;
              max-width: 2vw;
              max-height: 2vw;
            }
            @media only screen and (max-width: 600px) {
              .services-page .inner-page-intro img {
                min-width: 70vw;
                max-width: 70vw;
              }
              .our-services .section {
                display: flex;
                flex-direction: column;
              }
              .service-all-bullets {
                margin-top: 3vw;
                display: flex;
                flex-direction: column;
                grid-gap: 3vw;
                overflow: hidden;
              }
              .service-bullets {
                display: flex;
                flex-wrap: wrap;
                flex-direction: column;
                grid-gap: 5vw;
              }
              .service-name-box {
                grid-gap: 5vw;
                margin-top: 5vw;
                margin-bottom: 5vw;
              }
              .service-name-box h5 {
                font-size: 6vw;
                padding: 0vw 2vw;
              }
              .service-box-image img {
                min-width: 55vw;
                max-width: 55vw;
              }
              .seemore {
                grid-gap: 1.2vw;
                padding: 3vw 3vw;
                border-radius: 50vw;
              }
              .seemore h3 {
                font-size: 2.5vw;
                letter-spacing: 0.2vw;
                margin-left: 4vw;
              }
              .go-to-page {
                grid-gap: 1.2vw;
                padding: 3vw 5vw;
                border-radius: 50vw;
              }
              .go-to-page h3 {
                font-size: 2.5vw;
                letter-spacing: 0.2vw;
              }
              .plus-minus-icon img {
                min-width: 3.1vw;
                max-width: 3.1vw;
                margin-top: -0.1vw;
              }
              .service-all-bullets {
                grid-gap: 10vw !important;
                display: flex;
              }
              .service-bullets {
                max-width: 100%;
                display: flex;
                flex-direction: row;
                grid-gap: 10vw !important;
              }
              .service-bullet {
                max-width: 45%;
                min-width: unset;
              }
              .service-bullets h3 {
                font-size: 3vw;
                line-height: 1.3;
              }
              .section-indicator {
                top: -83vw;
              }
            }
          </style>
        </div>
        <div class="crm-page-css w-embed">
          <style>
            .services-indicator {
              position: relative;
            }
            .service-page-hero {
              margin-top: 8vw;
              margin-bottom: 8vw;
              display: flex;
              flex-direction: column;
              grid-gap: 5vw;
            }
            .service-page-heading {
              display: inline-flex;
              flex-direction: column;
              justify-content: start;
              align-items: start;
            }
            .page-cover-image img {
              min-width: 100%;
              max-width: 100%;
            }
            .aspect-box {
              background: #eee7e7;
              padding: 2.8vw;
              width: 22.5vw;
              border-radius: 1.5vw;
              display: flex;
              flex-direction: column;
              grid-gap: 2vw;
            }
            .aspect-box img {
              min-width: 5vw;
              max-width: 5vw;
            }
            .aspect-box h3 {
              font-size: 1.5vw;
              letter-spacing: -0.1vw;
              line-height: 1.1;
            }
            .aspects-section {
              display: flex;
              flex-direction: column;
              grid-gap: 3vw;
              margin-bottom: 8vw;
            }
            .integration {
              margin-top: 10vw;
              margin-bottom: 10vw;
            }
            .integration-boxes {
              display: flex;
              grid-gap: 2.5vw;
              margin-top: 4vw;
            }
            .integration-box {
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
              background-size: 100% 100%;
              border-radius: 1vw;
              height: 25vw;
              width: 30vw;
              display: flex;
              padding: 3vw;
              flex-direction: column;
              justify-content: space-between;
              align-items: start;
              color: var(--beige);
            }
            .integration-box p {
              color: var(--beige) !important;
              max-width: 85% !important;
            }
            .integration-box h3,
            .additional-box h3 {
              font-size: 1.5vw;
              line-height: 1.1;
            }
            .additional-boxes {
              display: flex;
              grid-gap: 2.5vw;
              flex-wrap: wrap;
            }
            .additional-box {
              border-radius: 1vw;
              border: 0.5px solid var(--black);
              height: 18vw;
              width: 26.6vw;
              display: flex;
              padding: 3vw;
              flex-direction: column;
              justify-content: space-between;
              align-items: start;
              color: var(--black);
            }
            .additional-box p {
              color: var(--black);
              max-width: 88%;
            }
            @media only screen and (max-width: 600px) {
              .service-page-hero {
                margin-top: 15vw;
                margin-bottom: -10vw !important;
                grid-gap: 10vw;
              }
              .service-page-hero h1 {
                font-size: 10vw;
              }
              .cms-intro {
                padding-top: 10vw;
              }
              .grid-line {
                display: flex !important;
                flex-direction: column;
              }
              .padding-top {
                padding-top: 15vw;
              }
              .aspect-box {
                padding: 8vw;
                width: 100%;
                border-radius: 3vw;
                grid-gap: 5vw;
                margin-bottom: 5vw;
              }
              .aspect-box img {
                min-width: 15vw;
                max-width: 15vw;
              }
              .aspect-box h3,
              .integration-box h3,
              .additional-box h3 {
                font-size: 4.5vw !important;
                max-width: 75%;
                line-height: 1.1;
              }
              .integration-boxes {
                display: flex;
                flex-direction: column;
                grid-gap: 2.5vw;
                margin-top: 4vw;
              }
              .integration-box {
                height: 65vw;
                width: 100%;
                display: flex;
                padding: 8vw;
                border-radius: 3vw;
              }
              .additional-boxes {
                grid-gap: 5vw;
              }
              .additional-box {
                height: auto;
                width: 100%;
                display: flex;
                padding: 8vw;
                border-radius: 3vw;
              }
            }
          </style>
        </div>
        <div class="contact-css w-embed">
          <style>
            .contact-page {
              padding-top: 12vw !important;
            }
            .split-contact {
              height: 67vh;
              display: flex;
            }
            .contact-right {
              flex: 1;
            }
            .contact-left {
              flex: 2;
            }
            .contact-left {
              display: flex;
              flex-direction: column;
              grid-gap: 5vw;
              height: 67vh;
              justify-content: space-between;
            }
            .contact-left h1 {
              font-size: 7vw;
              position: relative;
              left: -0.3vw;
            }
            .form {
              height: 67vh !important;
              display: flex;
              flex-direction: column;
              justify-content: space-between;
            }
            .contact-container {
              display: flex;
              justify-content: space-between;
              width: 100%;
            }
            .contact-column {
              flex: 1;
              display: flex;
              flex-direction: column;
              grid-gap: 1.5vw;
            }
            .contact-column img {
              min-width: 7vw;
              max-width: 7vw;
              margin-bottom: 1vw;
            }
            .contact-column h3 {
              font-size: 1.7em;
              letter-spacing: -0.05vw;
            }
            .label-text span {
              color: var(--red);
            }
            .form-field {
              border: none;
              background: transparent;
              border-bottom: 2px solid #eee7e7;
            }
            .message {
              height: 15vh !important;
            }
            .submit {
              background: linear-gradient(
                66deg,
                rgba(169, 45, 76, 1) 24%,
                rgba(95, 42, 87, 1) 100%
              );
              background-size: 100% 100%;
              border-radius: 1vw;
              width: 100%;
              padding: 2vw 0vw;
              font-size: 1.7vw;
            }
            .w-input,
            .w-select {
              padding: 0 !important;
              height: 7vh;
              font-size: 1.3vw !important;
              color: var(--mid-brown) !important;
            }
            @media only screen and (max-width: 600px) {
              .contact-page {
                padding-top: 25vw !important;
              }
              .split-contact {
                display: flex;
                flex-direction: column;
                grid-gap: 12vw;
              }
              .split-contact,
              .contact-left,
              .contact-right,
              .form {
                height: unset !important;
              }
              .contact-column {
                margin-top: 8vw;
              }
              .contact-left h1 {
                font-size: 11vw;
              }
              .form {
                margin-top: 5vw;
              }
              .contact-column {
                flex: unset;
                grid-gap: 5vw;
              }
              .contact-column img {
                min-width: 15vw;
                max-width: 15vw;
              }
              .contact-column h3 {
                font-size: 3.7em;
                letter-spacing: -0.05vw;
              }
              .label-text {
                font-size: 3vw;
                margin-bottom: 2vw;
                margin-top: 1vw;
              }
              .w-input,
              .w-select {
                padding: 0 !important;
                height: 13vw;
                font-size: 3vw !important;
                color: var(--mid-brown) !important;
              }
              .submit {
                margin-top: 3vw;
                padding: 7vw 0vw;
                font-size: 4.7vw;
              }
            }
          </style>
        </div>
      </div>
      <div id="hideheader" class="nav">
        <div
          class="menu-overlay"
        ></div>
        <div class="logo">
          <a id="pt-link" href="/" class="w-inline-block"
            ><img
              src="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/071bd535a5d6ba145d09d12b6a6116c9d40d381f/zone.svg"
              loading="lazy"
              alt=""
          /></a>
        </div>
        <div id="mega-burger" class="burger">
          <div
            data-w-id="c930a0fd-20aa-bb8b-cce2-ecaf1bbea19d"
            class="menu-trigger"
          ></div>
          <div class="menu-button">
            <div data-w-id="c930a0fd-20aa-bb8b-cce2-ecaf1bbea19f">
              MENU<br />close<br />menu
            </div>
          </div>
        </div>
        <div class="menu menu-hide">
          <a href="https://website2pdf-wheat.vercel.app/" id="menu-link" class="link">home</a
          ><a href="/" id="menu-link" class="link">coming soon!</a
          ><a href="/" id="menu-link" class="link">coming soon!</a
          ><a href="/" id="menu-link" class="link">Coming Soon!</a
          ><a href="https://aryazone.vercel.app/main/index.html" aria-current="page" class="nav-cta w--current"
            ><span>Portfolio</span></a
          >
        </div>
      </div>
      <div id="cursor" class="cursor"><div class="cursor__circle"></div></div>
    </div>
    <div id="page" class="page-content">
      <main class="page contact-page">
        <div class="split-contact">
          <div
            id="w-node-e62fe791-1366-b586-8fec-d03952df9902-b3eba1c6"
            class="contact-left"
          >
            <h1
              id="w-node-_2aeb8957-738e-c2b8-d5e7-7c8a626b93bb-b3eba1c6"
              class="text-container"
            >
       CONVERT NOW!
            </h1>
            <div
              id="w-node-c2f61ef1-8a02-2e2f-ac49-8b9f5e54c4f1-b3eba1c6"
              class="contact-container"
            >
              <div class="contact-column">
                <img
                  src="https://imgs.search.brave.com/hSpeoXXMlXflj4JgDACAZPq9i6l-8Xb71LLcMwuX8BY/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9wbmcu/cG5ndHJlZS5jb20v/cG5nLXZlY3Rvci8y/MDIyMDgyMS9vdXJt/aWQvcG5ndHJlZS1k/b25hdGlvbi1pY29u/LWRvbmF0ZS1kb25h/dGlvbi1kb2xsYXIt/dmVjdG9yLXBuZy1p/bWFnZV8xOTYyODc4/NC5wbmc"
                  loading="lazy"
                  alt="Donate Me"
                />
                <h3>DONATE ME</h3>
                <p>
                  Donate Me For More Tools <br />
                 <a href="https://saweria.co/Verrdryd"><h4>Click Here!</h4></a> 
                </p>
              </div>
              <div class="contact-column">
                <img
                  src="https://assets-global.website-files.com/6618e637b1708fa9ebdf54ae/662c93368a72a974e525b1e2_CHAT-WITH-US.svg"
                  loading="lazy"
                  alt=""
                />
                <h3>Chat with Me</h3>
                <p>+62-895-0112-8383<br />aryamaulana1230@gmail.com</p>
              </div>
            </div>
          </div>
          <div
            id="w-node-_6759740f-7fd6-b897-0078-7dc684c48115-b3eba1c6"
            class="contact-right"
          >
            <div id="w-node-_6759740f-7fd6-b897-0078-7dc684c4811a-b3eba1c6">
              <div class="w-form">
                <form
                  id="wf-form-Lead-from-Lot"
                  name="wf-form-Lead-from-Lot"
                  action="/convert"
                  method="post"
                  class="form"
                >
                  <div class="label">
                    <label for="name" class="label-text"
                      >Link Website<span>*</span></label
                    ><input
                      class="form-field w-input"
                      maxlength="256"
                      name="url"
                      placeholder="Enter website URL"
                      type="text"
                      required
                    />
                  </div>
                  <div class="label">
                    <label for="email" class="label-text"
                      >Filename<span>*</span></label
                    ><input
                      class="form-field w-input"
                      maxlength="256"
                      name="filename"
                      placeholder="PDF Name (without .pdf)"
                      type="text"
                      required
                    />
                  </div>
                  <!-- <div class="label">
                    <label for="Subject" class="label-text"
                      >subject<span>*</span></label
                    ><select
                      id="Subject"
                      name="Subject"
                      data-name="Subject"
                      class="form-field w-select"
                    >
                      <option value=""></option>
                      <option value="Support">Support</option>
                      <option value="Media &amp; PR">Media &amp; PR</option>
                      <option value="Partners &amp; Sponsers">
                        Partners &amp; Sponsers
                      </option>
                    </select>
                  </div> -->
                  <!-- <div class="label">
                    <label for="Message" class="label-text">message</label
                    ><input
                      class="form-field message w-input"
                      maxlength="256"
                      name="Message"
                      data-name="Message"
                      placeholder=""
                      type="text"
                      id="Message"
                    />
                  </div> -->
                  <input
                    type="submit"
                    data-wait="Please wait..."
                    class="submit w-button"
                    value="CONVERT"
                  />
                </form>
                <div class="success-message w-form-done">
                  <div>Your File Have Converted!</div>
                </div>
                <div class="error-message w-form-fail">
                  <div>
                    Oops! Something went wrong while converting the file.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          id="w-node-_289306ee-fe2d-9188-df75-ed50a5a81416-b3eba1c6"
          class="contact"
        >
          <div
            id="w-node-_289306ee-fe2d-9188-df75-ed50a5a81418-b3eba1c6"
            class="footer"
          >
            <div
              id="w-node-_289306ee-fe2d-9188-df75-ed50a5a81419-b3eba1c6"
              class="section grid"
            >
              <div
                id="w-node-_289306ee-fe2d-9188-df75-ed50a5a8141a-b3eba1c6"
                class="footer-logo"
              >
                <img
                  src="https://raw.githubusercontent.com/VoyagerXyroo/convertWEBSITEtoPDF_ASSETS/main/aryaB.png"
                  loading="lazy"
                  alt=""
                  class="image-2"
                />
              </div>
              <div id="w-node-_289306ee-fe2d-9188-df75-ed50a5a8141c-b3eba1c6">
                <div class="footer-column">
                  <div
                    id="w-node-bf58408c-b0d5-7f71-5ca8-1e6c2147ecae-2147ecad"
                    class="fc"
                  >
                    <!-- <h3>SERVICES</h3>
                    <div class="footer-menu">
                      <a
                        href="https://www.lt-serv.com/services#devops-solutions"
                        class="link"
                        >DevOps</a
                      ><a
                        href="https://www.lt-serv.com/services#data-management"
                        class="link"
                        >Data Management</a
                      ><a
                        href="https://www.lt-serv.com/services#enterprise-solutions"
                        class="link"
                        >Enterprise Solutions</a
                      ><a
                        href="https://www.lt-serv.com/services#quality-assurance"
                        class="link"
                        >Quality Assurance</a
                      ><a href="/crm" class="link">CRM Solutions</a
                      ><a
                        href="https://www.lt-serv.com/services#in-tech-solutions"
                        class="link"
                        >In-Tech Solutions</a
                      >
                    </div>
                  </div>
                  <div class="fc">
                    <h3>ADDRESS</h3>
                    <p>
                      12 Archiepiskopou Makariou <br />Avenue Ill, Office No.
                      201, ZAVOS <br />KRISTELLINA TOWER, 4000, Mesa
                      <br />Geitonia, Limassol, Cyprus
                    </p>
                  </div> -->
                  <div class="fc">
                    <h3>CONTACT</h3>
                    <p>aryamaulana1230@gmail.com<br />+62-895-0112-8383</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
    <div class="scripts">
      <div class="gsap w-embed w-script">
        <script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/gsap-latest-beta.min.js"></script>
        <script src="https://gsapfiles.netlify.app/scrambletextplugin.min.js"></script>
        <script src="https://gsapfiles.netlify.app/gsap.min.js"></script>
        <script src="https://gsapfiles.netlify.app/scrolltrigger.min.js"></script>
        <script src="https://gsapfiles.netlify.app/splittext.min.js"></script>

        <script>
          document.addEventListener("DOMContentLoaded", function () {
            // Initialize GSAP plugins
            gsap.registerPlugin(ScrollTrigger, SplitText, ScrambleTextPlugin);

            // Function to animate scramble text on hover
            function animateHoverScramble(textContainer, newText) {
              gsap.to(textContainer, {
                scrambleText: {
                  text: newText,
                  chars: "ABC*abc*123!*",
                  speed: 1,
                },
                ease: Linear.easeNone,
                duration: 0.5,
              });
            }

            // SplitText animation
            gsap.utils
              .toArray(".text-container")
              .forEach(function (textContainer, index) {
                var newText = textContainer.textContent.trim();

                // Calculate delay based on index to stagger animations
                var delay = index * 0.2; // Adjust delay as needed
                var duration = 1.2; // Duration for SplitText animation

                if (!textContainer.closest(".cta-text-block")) {
                  gsap.from(textContainer, {
                    scrollTrigger: textContainer,
                    duration: duration,
                    yPercent: 200,
                    ease: "power4.out",
                    skewY: 6,
                    opacity: 0,
                    onComplete: function () {
                      // ScrambleText animation
                      gsap.to(textContainer, {
                        scrambleText: {
                          text: newText,
                          chars: "ABC*abc*123!*", // Set scramble complexity with custom characters
                          speed: 1, // Set scramble speed
                        },
                        ease: Linear.easeNone,
                        duration: 0.5, // Duration for ScrambleText animation
                      });
                    },
                    delay: delay, // Apply staggered delay to the SplitText animation
                  });
                }

                // Hover animation
                textContainer.addEventListener("mouseover", function () {
                  animateHoverScramble(textContainer, newText);
                });
              });
          });
        </script>

        <script>
          document.addEventListener("DOMContentLoaded", function () {
            function showTitleAndAnimate(title) {
              gsap.registerPlugin(SplitText, ScrollTrigger);

              const childSplit = new SplitText(title, {
                type: "lines", // Split by lines
                linesClass: "split-child",
              });

              const parentSplit = new SplitText(title, {
                type: "lines", // Split by lines
                linesClass: "split-parent",
              });

              gsap.from(childSplit.lines, {
                scrollTrigger: {
                  trigger: title,
                  start: "top 120%",
                  end: "bottom 100%",
                  toggleActions: "play none none none",
                },
                duration: 1.2,
                yPercent: 200,
                ease: "power4.out",
                skewY: 6,
                stagger: 0.15,
                opacity: 0, // Start from opacity 0 to animate in
              });
            }

            const headings = gsap.utils.toArray(
              "h2, h3, h4, p, .footer-menu .link"
            );

            headings.forEach(function (title) {
              title.style.visibility = "hidden";
            });

            headings[0].style.visibility = "visible";
            showTitleAndAnimate(headings[0]);

            for (let i = 1; i < headings.length; i++) {
              setTimeout(function () {
                headings[i].style.visibility = "visible";
                showTitleAndAnimate(headings[i]);
              }, 0 * i);
            }
          });
        </script>

        <script>
          gsap.from(".splide__slide", {
            xPercent: 180,
            duration: 2,
            ease: "power4.out",
            scrollTrigger: {
              trigger: ".splide",
              start: "top 120%", // Adjusted to start animation earlier
              end: "bottom 100%", // Change this value as needed
            },
          });

          const dbwRowImages = document.querySelectorAll(".dbw-row-2 img");

          dbwRowImages.forEach((img) => {
            gsap.fromTo(
              img,
              {
                clipPath: "inset(30% 30% 30% 30%)", // Initial clip path
              },
              {
                clipPath: "inset(0% 0% 0% 0%)", // Final clip path
                duration: 1, // Duration of the animation
                ease: "power1.out", // Easing function
                scrollTrigger: {
                  trigger: img.parentElement, // Use the parent element as the trigger
                  start: "top 100%",
                  end: "bottom 80%",
                  scrub: 1.1,
                },
              }
            );
          });

          const projectBoxes = document.querySelectorAll(".recent-work-block");

          projectBoxes.forEach((box, index) => {
            const img = box.querySelector("img");

            gsap.fromTo(
              img,
              {
                y: 100,
                opacity: 0,
              },
              {
                opacity: 1,
                y: 0,
                ease: "power1.out",
                scrollTrigger: {
                  trigger: box,
                  start: "top 100%",
                  end: "bottom 100%",
                  scrub: 1,
                },
              }
            );
          });

          const whyBulletElements = document.querySelectorAll(".why-bullet");

          whyBulletElements.forEach((element) => {
            gsap.fromTo(
              element,
              {
                clipPath: "inset(0% 0% 100% 0%)", // Initial clip path
              },
              {
                clipPath: "inset(0% 0% 0% 0%)", // Final clip path
                duration: 1, // Duration of the animation
                ease: "power1.out", // Easing function
                scrollTrigger: {
                  trigger: element.parentElement, // Use the parent element as the trigger
                  start: "top 100%",
                  end: "bottom 80%",
                },
              }
            );
          });

          gsap.to(".services-page .inner-page-intro", {
            rotation: 360,
            scrollTrigger: {
              trigger: ".services-page .inner-page-intro",
              start: "top 100%",
              end: "bottom 0%",
              scrub: true,
            },
          });
        </script>
      </div>
      <div class="lenis w-embed w-script">
        <style>
          /*lenis -- IMPORTANT*/
          html {
            scroll-behavior: initial;
          }
          html,
          body {
            width: 100%;
            height: auto !important;
            min-height: 100%;
          }
        </style>
        <script src="https://assets-global.website-files.com/659fe92f193868b7c3f4da3b/65d84ab5a204cd113a363a4f_lenis-smooth.txt"></script>
        <script>
          const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
            direction: "vertical",
            smooth: true,
          });

          function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
          }

          requestAnimationFrame(raf);
        </script>

        <script>
          document.addEventListener("DOMContentLoaded", function () {
            var elements = document.querySelectorAll(
              ".recent-blog-block-text p"
            );
            var maxWords = 20;

            elements.forEach(function (element) {
              var text = element.textContent.trim();
              var words = text.split(/\s+/);

              if (words.length > maxWords) {
                var truncatedText = words.slice(0, maxWords).join(" ");
                element.textContent = truncatedText + "...";
              }
            });
          });
        </script>
      </div>
      <div class="cursor w-embed w-script">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

        <script>
          document.addEventListener("DOMContentLoaded", function () {
            const cursor = document.querySelector("#cursor");
            const cursorCircle = cursor.querySelector(".cursor__circle");
            const mouse = { x: -100, y: -100 }; // Set initial position off-screen
            let isMoving = false;
            gsap.set(cursor, { xPercent: -50, yPercent: -50 });

            const updateCoordinates = (e) => {
              mouse.x = e.clientX;
              mouse.y = e.clientY;
              isMoving = true; // Mouse is moving
            };

            const stopMoving = () => {
              isMoving = false; // Mouse is not moving (e.g., after click)
            };

            window.addEventListener("mousemove", updateCoordinates);

            const x = localStorage.getItem("cursorX");
            const y = localStorage.getItem("cursorY");

            if (x !== null && y !== null) {
              gsap.set(cursor, { x: x, y: y });
            }

            window.addEventListener("beforeunload", () => {
              localStorage.setItem("cursorX", mouse.x);
              localStorage.setItem("cursorY", mouse.y);
            });

            function animateCursor() {
              if (isMoving) {
                gsap.to(cursor, {
                  duration: 0.5,
                  x: mouse.x,
                  y: mouse.y,
                  ease: "power2.out",
                });
              }
              requestAnimationFrame(animateCursor);
            }

            animateCursor();

            window.addEventListener("mousedown", stopMoving);
            window.addEventListener("mouseup", updateCoordinates); // Resume tracking after mouseup
          });

          jQuery(document).ready(function ($) {
            // Add hover effect to all 'a' elements, excluding those inside '.recent-work-links'
            $("a")
              .not(".recent-work-links a")
              .hover(
                function () {
                  $("#cursor")
                    .addClass("overlay")
                    .removeClass("explore-overlay"); // Remove explore-overlay class if present
                },
                function () {
                  $("#cursor").removeClass("overlay");
                }
              );

            // Add class 'explore-overlay' to the cursor when hovering over 'a' elements inside '.recent-work-links'
            $(".splide__track").hover(
              function () {
                $("#cursor").addClass("explore-overlay").removeClass("overlay"); // Remove overlay class if present
              },
              function () {
                $("#cursor").removeClass("explore-overlay");
              }
            );

            $(".sub-form").hover(
              function () {
                $("#cursor").addClass("overlay");
              },
              function () {
                $("#cursor").removeClass("overlay");
              }
            );
          });
        </script>
      </div>
      <div class="slider-js w-embed w-script">
        <style>
          .splide__track {
            overflow: visible;
          }
          .splide__arrows,
          .splide__pagination {
            display: none;
          }
        </style>
        <script src="https://cdn.jsdelivr.net/npm/@splidejs/splide@3.2.2/dist/js/splide.min.js"></script>

        <script>
          function slider1() {
            let splides = $(".slider1");
            for (
              let i = 0, splideLength = splides.length;
              i < splideLength;
              i++
            ) {
              new Splide(splides[i], {
                // Desktop on down
                perPage: 3,
                perMove: 1,
                focus: 0, // 0 = left and 'center' = center
                type: "slide", // 'loop' or 'slide'
                gap: "5vw", // space between slides
                arrows: "slider", // 'slider' or false
                pagination: "slider", // 'slider' or false
                speed: 600, // transition speed in miliseconds
                dragAngleThreshold: 60, // default is 30
                autoWidth: false, // for cards with differing widths
                rewind: false, // go back to beginning when reach end
                rewindSpeed: 400,
                waitForTransition: false,
                updateOnMove: true,
                trimSpace: false, // true removes empty space from end of list
                breakpoints: {
                  991: {
                    // Tablet
                    perPage: 2,
                    gap: "5vw",
                  },
                  767: {
                    // Mobile Landscape
                    perPage: 1,
                    gap: "3vw",
                  },
                  479: {
                    // Mobile Portrait
                    perPage: 1,
                    gap: "3vw",
                  },
                },
              }).mount();
            }
          }
          slider1();
        </script>
      </div>
      <div class="extra w-embed w-script">
        <script>
          if (window.innerWidth > 600) {
            const nav = document.querySelector(".nav");
            let lastScrollTop = 0;

            window.addEventListener("scroll", function () {
              // Toggle 'fixed' class based on scroll position
              if (window.scrollY > 350) {
                // Changed from 350 to 250
                nav.classList.add("fixed");
              } else {
                nav.classList.remove("fixed");
              }

              // Toggle 'hide' class based on scroll direction
              var st = window.pageYOffset || document.documentElement.scrollTop;
              if (st > lastScrollTop && st > 150) {
                // Changed from 350 to 250
                nav.classList.add("hide");
              } else {
                nav.classList.remove("hide");
              }
              lastScrollTop = st <= 0 ? 0 : st;
            });
          }
        </script>

        <script>
          var screenWidth = window.innerWidth;
          var threshold = 600;

          window.addEventListener("resize", function () {
            var newWidth = window.innerWidth;

            // Check if the screen width crosses the threshold
            if (
              (screenWidth < threshold && newWidth >= threshold) ||
              (screenWidth >= threshold && newWidth < threshold)
            ) {
              location.reload();
            }

            // Update the stored screen width
            screenWidth = newWidth;
          });
        </script>
      </div>
    </div>
    <script
      src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=6618e637b1708fa9ebdf54ae"
      type="text/javascript"
      integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
      crossorigin="anonymous"
    ></script>
    <script
      src="https://assets-global.website-files.com/6618e637b1708fa9ebdf54ae/js/lot-experience.d22f9b87f.js"
      type="text/javascript"
    ></script>
    <script type="text/javascript">
      !(function () {
        if (!window.UnicornStudio) {
          window.UnicornStudio = { isInitialized: !1 };
          var i = document.createElement("script");
          (i.src = "https://cdn.unicorn.studio/v1.2.0/unicornStudio.umd.js"),
            (i.onload = function () {
              window.UnicornStudio.isInitialized ||
                (UnicornStudio.init(),
                (window.UnicornStudio.isInitialized = !0));
            }),
            document.getElementsByTagName("head")[0].appendChild(i);
        }
      })();
    </script>
    <style>
      .splide__track {
        overflow: visible;
      }
      .splide__arrows,
      .splide__pagination {
        display: none;
      }
      .splide__slide {
        margin: unset !important;
        width: unset !important;
      }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/@splidejs/splide@3.2.2/dist/js/splide.min.js"></script>

    <script>
      function slider1() {
        let splides = $(".slider1");
        for (let i = 0, splideLength = splides.length; i < splideLength; i++) {
          new Splide(splides[i], {
            perPage: 3,
            perMove: 1,
            focus: 0,
            type: "slide",
            gap: "5vw",
            arrows: "slider",
            pagination: "slider",
            speed: 1000,
            dragAngleThreshold: 60,
            autoWidth: false,
            rewind: false,
            rewindSpeed: 1000,
            waitForTransition: false,
            updateOnMove: true,
            trimSpace: true,
          }).mount();
        }
      }
      slider1();
    </script>

    <script>
      $(document).ready(function () {
        $("body").addClass("body-loaded");
        gsap.set(".page", { y: 300 });
        gsap.to(".page", {
          y: 0,
          duration: 1.7,
          delay: -0.45,
          ease: "expo.inOut",
        });
        gsap.set("#cursor", { opacity: 0, scale: 0 });
        gsap.to("#cursor", {
          opacity: 1,
          scale: 1,
          duration: 0.8,
          ease: "power2.inOut",
        });
        $("#cursor").css("display", "block");
      });

      $("a").click(function (event) {
        var url = $(this).attr("href");
        if (
          url.startsWith("#") ||
          url.startsWith("mailto:") ||
          url.startsWith("https://wa.me")
        ) {
          return;
        }
        event.preventDefault();
        $("body").addClass("body-loader");

        gsap.to("#page", { opacity: 0.8, duration: 0.5, ease: "power2.inOut" });

        gsap.to("#cursor", {
          opacity: 0,
          scale: 0,
          duration: 0.5,
          ease: "power2.inOut",
        });
        setTimeout(() => (window.location.href = url), 1000);
      });

      window.onpageshow = function (event) {
        if (event.persisted) {
          window.location.reload();
        }
      };
    </script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script>
      jQuery(document).ready(function () {
        // Smooth scrolling for anchor links within the same page
        jQuery('a[href*="#"]:not([href="#"])').click(function () {
          var target = jQuery(this.hash);
          if (target.length) {
            jQuery("html, body").animate(
              {
                scrollTop: target.offset().top,
              },
              500,
              "swing"
            );
            return false;
          }
        });

        // Smooth scrolling for anchor links coming from a different page
        var hash = window.location.hash;
        if (hash.length > 0) {
          jQuery(window).on("load", function () {
            var target = jQuery(hash);
            if (target.length) {
              jQuery("html, body").animate(
                {
                  scrollTop: target.offset().top,
                },
                500,
                "swing"
              );
            }
          });
        }
      });
    </script>
  </body>
</html>

'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(form_html)

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form['url']
    filename = request.form['filename']

    # Konversi URL menjadi PDF menggunakan pdfcrowd
    client = pdfcrowd.HtmlToPdfClient('Verrdryd', '95e498806f86b98f79226fdfdd8f62da')
    pdf = io.BytesIO()
    client.convertUrlToStream(url, pdf)
    pdf.seek(0)

    # Kirimkan file PDF sebagai respons unduhan
    return send_file(
        pdf,
        attachment_filename=f"{filename}.pdf",
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
