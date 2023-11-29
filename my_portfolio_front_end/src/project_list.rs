use yew::prelude::*;
use yew::services::fetch::{FetchService, FetchTask, Request, Response};

use crate::project_model::Project;

pub struct ProjectList {
    link: ComponentLink<Self>,
    projects: Vec<Project>,
    fetch_task: Option<FetchTask>
}

pub enum Msg {
    ProjectsLoaded(Vec<Project>)
}

impl Component for ProjectList {
    type Message = Msg;
    type Properties = ();

    fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
        let fetch_task = Self::fetch_projects(&link);
        Self {
            link,
            projects: Vec::new(),
            fetch_task: 
        }
    }
}