mod asset_manager;
use asset_manager::AssetManager;
use std::collections::HashMap;

// tokio let's us use "async" on our main function
#[tokio::main]
async fn main() {
    let s = String::from("assert");
    let test = AssetManager::new(&s);
    let result = reqwest::get("https://api.spotify.com/v1/search").await;
    test.print_pn();
    println!("{:?}", result);
}

