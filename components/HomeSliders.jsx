'use client';
import React from 'react';
import { Carousel } from '@mantine/carousel';
import { useRef } from 'react';
import Autoplay from 'embla-carousel-autoplay';
import '@mantine/carousel/styles.css';

const HomeSliders = () => {
    const autoplay = useRef(Autoplay({ delay: 5000 }));

    return (
        <div className="carousel-container">
            <Carousel
                withIndicators
                plugins={[autoplay.current]}
                onMouseEnter={autoplay.current.stop}
                onMouseLeave={autoplay.current.reset}
                slideSize="100%"
                slideGap="md"
                loop
                align="start"
                controlsOffset="xs"
                controlSize={30}
            >
                {[1, 2, 3, 4, 5, 6, 7].map((num) => (
                    <Carousel.Slide key={num}>
                        <img
                            src={`https://www.gov.br/mec/pt-br/pe-de-meia/card-${num}.jpg`}
                            alt={`Slide ${num}`}
                            className="carousel-image"
                        />
                    </Carousel.Slide>
                ))}
            </Carousel>
        </div>
    );
};

export default HomeSliders;
