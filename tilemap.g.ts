// Código generado automáticamente. No editar.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile3 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile4 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile7 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "nivel":
            case "nivel1":return tiles.createTilemap(hex`1000100003030303030303030303030303030303030303030303030404040403030303030304040404040404040404040303030303040404010101010101040404030303030404040101010202010404040303030304040401010202010104040403030303040401010202020201010404030303030404010102020202020104040303030304040101020202020201040403030303040404010102020202010404040303030304040401010201020104040403030303030404040101010101040404040303030304040404040404040404040403030303030404040404040404040404030303030303030303030303030303030303030303030303030303030303030303`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . 2 2 2 2 . . . . . . . . . . 
. . . . 2 2 2 2 2 2 2 . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . 2 . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,myTiles.tile2,myTiles.tile3,myTiles.tile4,myTiles.tile7], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
            case "miMosaico0":
            case "tile2":return tile2;
            case "miMosaico1":
            case "tile3":return tile3;
            case "miMosaico2":
            case "tile4":return tile4;
            case "miMosaico5":
            case "tile7":return tile7;
        }
        return null;
    })

}
// Código generado automáticamente. No editar.
