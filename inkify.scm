(define
    (script-fu-inkify inputFileName outputFileName)
    (let*
        ; Open a pre-defined image as theImage
        (
        
            (theImage
                (car
                    (
                        file-jpeg-load
                        RUN-NONINTERACTIVE
                        inputFileName
                        "Floki.jpg"
                    )
                )
            )  
        )
        ; Convert theImage to indexed mode
        (gimp-image-convert-indexed
            theImage                    ; Image to convert
            CONVERT-DITHER-FS           ; Dithering method to use during the conversion
            CONVERT-PALETTE-CUSTOM      ; Palette to use during the conversion
            3                           ; Number of colours to convert to
            FALSE                        ; Dither to give appearance of transparency
            FALSE                       ; Remove unused/duplicate colours
            "InkyPalette.gpl"             ; Name of the custom palette to use
        )
        ; Save the image as a PNG
        (file-png-save-defaults
            RUN-NONINTERACTIVE
            theImage
            (car (gimp-image-get-active-layer theImage))
            outputFileName
            outputFileName
        )
        (gimp-image-delete
            theImage
        )

    )
)
