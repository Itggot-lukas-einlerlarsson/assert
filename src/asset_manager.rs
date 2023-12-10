pub struct AssetManager {
    programname : String, 
    assets : Vec<String>
}

impl AssetManager {
    pub func run(pn : &String) {
        return AssetManager {
            programname : String::from(pn),
            assets : Vec::new()
        }   
    }
}