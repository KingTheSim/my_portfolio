use yew::Properties;

#[derive(Debug, Clone, PartialEq, Properties)]
pub struct Project {
    pub name: String,
    pub language: String,
    pub description: String
}