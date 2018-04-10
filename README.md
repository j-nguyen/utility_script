# Utility Scripts

These are general scripts to help assist with GitHub. It's to assist on rebasing, pulling, and doing pull requests. I use this since I'm a lazy person. 

You can add this on with build-like scripts and setup scripts so that it feels more complete. At the moment, it's at its barebones, since it's really only being used as a git-cli option.

Anyway, feel free to use it.

# Setting it up

## Configure config.json

Right now, it depends on a configuration file, which holds up all your things. Here's how it looks like:

```json
{
  "user": "your user github",
  "token": "your personal access token",
  "repo": "The Repo's name",
  "owner": "The owner of the repo"
}
```

Save this into the directory.

## Configuring your directory

Make sure all these scripts are under `bin/`. This is how it works. Call the `workflow.py`, from your project directory, so you'd run `bin/workflow.py`, in order to get started.

An example of a could project directory could look like:

```
├── bin
│   ├── workflow.py
├── project files
└── .gitignore
```