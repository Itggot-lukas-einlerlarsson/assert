pub struct AssetManager {
    programname : String,
    assets : Vec<String>
}

impl AssetManager {
    pub fn new(pn : &String) -> AssetManager {
        return AssetManager {
            programname : String::from(pn),
            assets : Vec::new()
        }
    }
    pub fn print_pn(&self) {
        println!("Hej from {}", self.programname);
    }
}
