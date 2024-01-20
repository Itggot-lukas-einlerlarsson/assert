mod asset_manager;
use asset_manager::AssetManager;

fn main() {
    let s = String::from("assert");
    let test = AssetManager::new(&s);
    test.print_pn();
    println!("Hello, world!");
}
